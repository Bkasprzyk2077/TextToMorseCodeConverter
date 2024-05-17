from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
import os

import logic

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap5(app)


class TextToMorse(FlaskForm):
    text = TextAreaField(label='Plain text', validators=[DataRequired()], id="plain_text")
    form_id = HiddenField('form_id', default='form1')
    submit1 = SubmitField(label="Convert to morse")
    copy_text = SubmitField('Copy',
                       render_kw={'onclick': 'copyTextToClipboard()', 'type': 'button', 'class': 'btn btn-dark'})


class MorseToText(FlaskForm):
    morse = TextAreaField(label='Morse code', validators=[DataRequired()], id="morse_code")
    form_id = HiddenField('form_id', default='form2')
    submit2 = SubmitField(label="Convert to text")
    copy_morse = SubmitField('Copy', render_kw={'onclick': 'copyMorseToClipboard()', 'type': 'button', 'class': 'btn btn-dark'})
    play_sound = SubmitField('Play', render_kw={'onclick': 'readMorse()', 'type': 'button', 'class': 'btn btn-success'})


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", text_to_morse=TextToMorse(), morse_to_text=MorseToText())
    else:
        if request.form.get('form_id') == "form1":
            morse = logic.convert_to_morse(request.form.get("text"))
            morse_to_text_form = MorseToText()
            morse_to_text_form.morse.data = morse
            morse_to_text_form.form_id.data = "form2"
            return render_template("index.html", text_to_morse=TextToMorse(), morse_to_text=morse_to_text_form)
        elif request.form.get('form_id') == "form2":
            text = logic.convert_to_text(request.form.get("morse"))
            text_to_morse_form = TextToMorse()
            text_to_morse_form.text.data = text
            text_to_morse_form.form_id.data = "form1"
            return render_template("index.html", text_to_morse=text_to_morse_form, morse_to_text=MorseToText())


@app.route("/text_to_morse", methods=["GET"])
def text_to_morse_json():
    text_to_translate: str = request.args.get("text")
    morse = logic.convert_to_morse(text_to_translate)
    return jsonify(text=text_to_translate, morse=morse)


@app.route("/morse_to_text", methods=["GET"])
def morse_to_text_json():
    morse_to_translate: str = request.args.get("morse")
    text = logic.convert_to_text(morse_to_translate)
    return jsonify(text=text, morse=morse_to_translate)


if __name__ == '__main__':
    app.run(debug=True)
