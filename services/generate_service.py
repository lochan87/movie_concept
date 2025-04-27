from config.gemini_config import configure_gemini
from services.prompt import build_prompt
from services.sentiment_analysis_service import analyze_character_tones, extract_and_analyze_script, analyze_visual_descriptions
from models.bert_sentiment import analyze_sentiment
from utils.helpers import split_sections
from utils.format import print_pretty_response

def generate_movie_content(model, storyline, genre, include_script=False, include_visuals=False, indian_content=False, language="english"):
    sentiment = analyze_sentiment(storyline)
    mood_description = "inspirational or uplifting" if sentiment == "positive" else "dark or emotional" if sentiment == "negative" else "balanced or calm"

    prompt = build_prompt(storyline, genre, mood_description, language, include_script, include_visuals, indian_content)
    try:
        response = model.generate_content(prompt)
        response_text = response.text

        sections = split_sections(response_text)
        response = print_pretty_response(response_text)
        character_tones = {}
        dialogue_sentiments = {"positive": 0, "negative": 0}
        visual_sentiments = {"positive": 0, "negative": 0}

        if sections["main_characters"]:
            character_tones = analyze_character_tones(sections["main_characters"])

        if include_script and sections["script"]:
            dialogue_tone_list = extract_and_analyze_script(sections["script"])
            dialogue_sentiments = {
                "positive": dialogue_tone_list.count("positive"),
                "negative": dialogue_tone_list.count("negative"),
                "neutral": dialogue_tone_list.count("neutral")
            }

        if include_visuals and sections["visuals"]:
            visual_tone_list = analyze_visual_descriptions(sections["visuals"])
            visual_sentiments = {
                "positive": visual_tone_list.count("positive"),
                "negative": visual_tone_list.count("negative"),
                "neutral": visual_tone_list.count("neutral")
            }

        return {
            "response_text": response,
            "character_tones": character_tones,
            "dialogue_sentiments": dialogue_sentiments,
            "visual_sentiments": visual_sentiments
        }

    except Exception as e:
        print(f"🚨 Error: {e}")
        return None
