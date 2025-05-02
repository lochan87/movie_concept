# 🎬 Movie Concept Generator

The **Movie Concept Generator** is an AI-powered creative tool that generates unique movie ideas based on a user-provided storyline and genre. It enhances output with options like script generation, visual descriptions, and Indian-language content. Powered by **DistilBERT**, it performs deep tone and script analysis to deliver high-quality creative results.  
📥 A user can also **download the generated content** in `.txt` format for offline use or sharing.

---

## ✨ Features

- 🧾 **Custom Inputs**:
  - Storyline
  - Genre
  - Include Script (Yes/No)
  - Include Visuals (Yes/No)
  - Include Indian Content (Yes/No → Language: English, Hindi, Kannada)

- 🧠 **AI Capabilities**:
  - Character tone analysis using **DistilBERT**
  - Script and visual analysis
  - Intelligent title and summary generation

- 📤 **Outputs**:
  - 🎬 Title
  - 👥 Main Characters
  - 📝 Long Summary
  - 🎭 Optional: Full script & visual descriptions

---

## 🛠️ Technologies Used

- **Python 3**
- **Transformers** (HuggingFace's `DistilBERT`)
- **Flask** (Frontend)
- **HTML, CSS, Bootstrap** (For UI if web-based)

---

## 📦 Installation

Follow the steps below to set up and run the Movie Concept Generator locally:

1. **Clone the Repository**
```bash
   git clone https://github.com/lochan87/movie_concept.git
   cd movie_concept
```
2. **(Optional) Create a Virtual Environment**
  python -m venv venv
  source venv\Scripts\activate
3. **Install Dependencies**
  pip install -r requirements.txt
4. **Run the Application**
  python app.py

---

## 🚀 How to Use

1. Launch the app via the command line.
2. In the web UI:
    - 🧾 **Enter a storyline**
    - 🎭 **Select a genre**
    - ✅ **Choose options:**
      - Include Script  
      - Include Visuals  
      - Include Indian Content → Select Language (**Hindi**, **Kannada**, or **English**)
3. Click the **"Generate"** button.
4. View the output:
    - 🎬 **Movie Title**
    - 👥 **Main Characters**
    - 📝 **Long Summary**
    - 🧾 **Script** (if selected)
    - 🖼️ **Visual Descriptions** (if selected)
5. ⬇️ **Download the generated content** as a `.txt` file for offline access or sharing.

---

## 🧠 AI Models Used

The project uses the **DistilBERT** model from Hugging Face Transformers, a distilled version of BERT, for efficient and contextual analysis of generated content.

### Applications of DistilBERT in this Project:

- **Character Tone Analysis**  
  Understands the emotional tone of dialogue and personality traits of characters.

- **Script Analysis**  
  Checks the narrative flow, cohesion, and dramatic structure of the screenplay.

- **Visual Analysis**  
  Interprets text to create coherent visual themes and cinematic mood descriptions.

🔗 **Model Used:** [DistilBERT Base Uncased](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
