from dotenv import load_dotenv
import os
import google.generativeai as genai

def get_api_key():
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the .env file")
    return GEMINI_API_KEY

def configure_gemini():
    try:
        genai.configure(api_key=get_api_key())
        model = genai.GenerativeModel("gemini-2.0-flash")
        return model
    except Exception as e:
        print(f"❌ Gemini setup failed: {e}")
        exit(1)
