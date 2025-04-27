from flask import Flask, render_template, request
from config.gemini_config import configure_gemini
from services.generate_service import generate_movie_content

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = None
    character_tones = None
    dialogue_sentiments = None
    visual_sentiments = None

    if request.method == "POST":
        storyline = request.form.get("storyline")
        genre = request.form.get("genre")
        include_script = request.form.get("include_script") == "yes"
        include_visuals = request.form.get("include_visuals") == "yes"
        indian_content = request.form.get("indian_content") == "yes"
        language = request.form.get("language") if indian_content else "english"

        model = configure_gemini()
        if model:
            results = generate_movie_content(
                model,
                storyline=storyline,
                genre=genre,
                include_script=include_script,
                include_visuals=include_visuals,
                indian_content=indian_content,
                language=language
            )

            if results:
                output = results["response_text"]
                character_tones = results["character_tones"]
                dialogue_sentiments = results["dialogue_sentiments"]
                visual_sentiments = results["visual_sentiments"]
        else:
            output = "Failed to configure model. Check API Key."

    return render_template("index.html", output=output, character_tones=character_tones, dialogue_sentiments=dialogue_sentiments, visual_sentiments=visual_sentiments)

if __name__ == "__main__":
    app.run(debug=True)
