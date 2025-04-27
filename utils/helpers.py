def split_sections(response_text):
    sections = {
        "title": "",
        "summary": "",
        "main_characters": "",
        "script": "",
        "visuals": ""
    }

    current_section = None

    for line in response_text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.lower().startswith("title") or "movie title" in line.lower():
            current_section = "title"
        elif line.lower().startswith("long summary") or "summary" in line.lower():
            current_section = "summary"
        elif line.lower().startswith("main characters") or "characters" in line.lower():
            current_section = "main_characters"
        elif line.lower().startswith("a long script") or "script" in line.lower():
            current_section = "script"
        elif line.lower().startswith("visual description") or "visuals" in line.lower() or "visual" in line.lower():
            current_section = "visuals"
        else:
            if current_section:
                sections[current_section] += line + "\n"

    return sections
