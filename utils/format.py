import re

def format_script_block(text):
    text = re.sub(r'<center>(.*?)<\/center>', r'\n🎭 \1\n', text)
    text = re.sub(r'^\s*>\s?', '    ', text, flags=re.MULTILINE)
    text = re.sub(r'^(INT\.|EXT\.).*$', lambda m: f"\n🎬 {m.group(0).upper()}\n" + "-"*60, text, flags=re.MULTILINE)
    text = re.sub(r'VISUALS\s*:\s*', '\n📷 VISUAL: ', text)
    text = re.sub(r'^\s*(\w+(?: \w+)*):?\s*$', r'🎙️ \1:', text, flags=re.MULTILINE)
    return text.strip()

def clean_text(text):
    text = re.sub(r'\*{1,2}', '', text)
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()

def print_pretty_response(response_text):
    response_text = clean_text(response_text)
    output = ""

    # Title
    title_match = re.search(r'Title\s*[:\-]?\s*(.*)', response_text, re.IGNORECASE)
    if title_match:
        output += f"🎬 Title: {title_match.group(1).strip()}\n"

    # Long Summary
    summary_match = re.search(r'Long Summary\s*[:\-]?\s*(.*?)(?:Main characters|Characters|$)', response_text, re.IGNORECASE | re.DOTALL)
    if summary_match:
        output += "\n📝 Summary:\n" + "-"*60 + "\n"
        output += summary_match.group(1).strip() + "\n"

    # Main Characters
    characters_match = re.search(r'(Main characters|Characters)\s*[:\-]?\s*(.*?)(?:Script|Dialogues|Visuals|$)', response_text, re.IGNORECASE | re.DOTALL)
    if characters_match:
        output += "\n🧑‍🤝‍🧑 Main Characters:\n" + "-"*60 + "\n"
        characters = characters_match.group(2).strip().split("\n")
        for c in characters:
            if ":" in c:
                name, desc = c.split(":", 1)
                output += f" - {name.strip()}: {desc.strip()}\n"
            else:
                output += f" - {c.strip()}\n"

    # Script
    script_match = re.search(r'(Script|Dialogues)\s*[:\-]?\s*(.*?)(?:Visuals|Visual Descriptions|$)', response_text, re.IGNORECASE | re.DOTALL)
    if script_match:
        output += "\n🎭 Script:\n" + "-"*60 + "\n"
        script = script_match.group(2).strip()
        output += format_script_block(script) + "\n"

    # Visuals
    visuals_match = re.search(r'(Visuals|Visual Description)\s*[:\-]?\s*(.*)', response_text, re.IGNORECASE | re.DOTALL)
    if visuals_match:
        output += "\n🎨 Visual Descriptions:\n" + "-"*60 + "\n"
        output += visuals_match.group(2).strip() + "\n"

    return output.strip()
