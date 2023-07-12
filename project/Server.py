from flask import Flask, request, render_template
from translator import english_to_french_translate, french_to_english_translate

app = Flask("My First Flask Application")


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = english_to_french_translate(textToTranslate)
    
    return translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = french_to_english_translate(textToTranslate)
    
    return translated_text



if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000