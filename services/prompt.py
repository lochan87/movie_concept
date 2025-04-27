def build_prompt(storyline, genre, mood_description, language, include_script, include_visuals, indian_content):
    lang_instruction = ""
    if language.lower() == "hindi":
        lang_instruction = "\nPlease write all content in Hindi."
    elif language.lower() == "kannada":
        lang_instruction = "\nPlease write all content in Kannada."

    prompt = f"""
        Create a movie concept with:
        - Storyline: {storyline}
        - Genre: {genre}
        - Mood: {mood_description}
        - Language: {language.capitalize()}
        {lang_instruction}

        Include:
        1. Title
        2. Long Summary
        3. Main characters with descriptions
    """

    if include_script:
        prompt += "\n4. A long script with dialogues"
    if include_visuals:
        prompt += "\n5. Visual descriptions for key scenes"
    if indian_content:
        prompt += "\n6. Let the movie concept be related to Indians and Indian cultural references and elements"

    return prompt
