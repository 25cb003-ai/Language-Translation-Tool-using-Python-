from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

@app.route("/", methods=["GET", "POST"])
def index():

    translated_text = ""

    if request.method == "POST":

        text = request.form["text"]

        source = request.form["source"]

        target = request.form["target"]

        try:
            translated_text = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

        except Exception as e:
            translated_text = str(e)

    return render_template(
        "index.html",
        languages=languages.keys(),
        translated_text=translated_text
    )

if __name__ == "__main__":
    app.run(debug=True)
