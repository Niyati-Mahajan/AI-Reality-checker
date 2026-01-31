# AI Reality Checker 🕵️‍♂️✨

An AI-powered web application that verifies rumors, news headlines, and claims using Google's Gemini 2.5 Flash model. Built for the Gemini Hackathon.

## Features
- **Instant Verification**: Analyzes claims for truthfulness.
- **Confidence Score**: Displays how certain the AI is about the verdict.
- **Source Citations**: Categorizes sources into News, Official, and Context.
- **Gemini UI**: A modern, glassmorphism-inspired interface with Dark/Light mode.

## Tech Stack
- **Frontend**: HTML5, CSS3 (Glassmorphism, Animations), JavaScript
- **Backend**: Python, Flask
- **AI Model**: Google Gemini 2.5 Flash (`google-genai` SDK)

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your API key:
   - Windows: `set GOOGLE_API_KEY=your_key`
   - Mac/Linux: `export GOOGLE_API_KEY=your_key`
4. Run the app:
   ```bash
   python app.py
   ```