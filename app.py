from flask import Flask, render_template, request
from google import genai
from google.genai import errors

app = Flask(__name__)

# Gemini client (uses API key or ADC)
client = genai.Client()

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        claim = request.form.get("claim")

        if not claim:
            return render_template("index.html", result="⚠️ Please enter a claim.")

        prompt = f"""
        You are an AI Reality Checker.
        Verify the following claim.
        Provide a confidence score (0-100%) representing how certain you are.
        Also provide key sources categorized by type.
        Respond in this format:
        Verdict: [True/False/Partially True]
        Confidence: [Percentage]%
        Explanation: [Short explanation]
        Sources:
        📰 News: [Major news coverage]
        🧾 Official: [Official statements or verified posts]
        📚 Context: [Contextual analysis or background]

        Claim: {claim}
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            result = response.text
        except errors.ClientError as e:
            if e.code == 429:
                result = "⚠️ API Quota Exceeded. Please wait a minute and try again."
            else:
                result = f"An error occurred: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
