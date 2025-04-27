from models.bert_sentiment import analyze_sentiment
from textblob import TextBlob
import re

def analyze_character_tones(script_text):
    """
    Analyzes character tones based on dialogue sentiment polarity.

    Args:
    - script_text: The full movie script text as a string.

    Returns:
    - character_tones: A dictionary mapping character names to their respective tone (Positive, Negative, Neutral).
    """
    # Initialize empty dictionary to store character tones
    character_tones = {}

    # Split the script into lines
    lines = script_text.split('\n')

    for line in lines:
        # Check if the line is in the format "CHARACTER: dialogue"
        if ':' in line:
            # Remove any markdown-style formatting (e.g., bold or italic characters)
            line = re.sub(r'\*{1,2}', '', line)
            parts = line.split(':', 1)
            character = parts[0].strip()
            dialogue = parts[1].strip()

            if character and dialogue:
                # Use TextBlob to analyze sentiment polarity of the dialogue
                analysis = TextBlob(dialogue)
                polarity = analysis.sentiment.polarity

                # Classify tone based on polarity score
                if polarity > 0.3:
                    tone = 'Positive'
                elif polarity < -0.3:
                    tone = 'Negative'
                else:
                    tone = 'Neutral'

                # Save the tone for the character (if multiple dialogues, override or aggregate)
                character_tones[character] = tone

    return character_tones


def extract_and_analyze_script(script_text):
    """
    Analyzes sentiment of each line of dialogue in the script.

    Args:
    - script_text: The full script of the movie as a string.

    Returns:
    - dialogue_tones: A list of sentiment labels (Positive, Negative, Neutral) for each dialogue.
    """
    lines = script_text.split("\n")
    dialogue_tones = []

    for line in lines:
        if ":" in line:
            # Extract dialogue part
            _, dialogue = line.split(":", 1)
            # Use the custom sentiment analysis model to detect the tone of the dialogue
            tone = analyze_sentiment(dialogue.strip())
            dialogue_tones.append(tone)

    return dialogue_tones


def analyze_visual_descriptions(visual_block):
    """
    Analyzes the sentiment of visual scene descriptions.

    Args:
    - visual_block: A string containing the scene descriptions.

    Returns:
    - scene_tones: A list of sentiment labels (Positive, Negative, Neutral) for each scene description.
    """
    lines = visual_block.split("\n")
    scene_tones = []

    for line in lines:
        if line.strip():
            # Use custom sentiment analysis to evaluate scene description tones
            tone = analyze_sentiment(line.strip())
            scene_tones.append(tone)

    return scene_tones
