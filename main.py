from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
import os

import logic

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap5(app)


class TextForm(FlaskForm):
    text = TextAreaField(label='Text', validators=[DataRequired()])
    from_to = SelectField(label='Converting from to', choices=["text to morse", "morse to text"],
                          validators=[DataRequired()])
    submit = SubmitField(label="Convert")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index2.html", form=TextForm(), text="")
    else:
        if request.form.get("from_to") == "text to morse":
            text = logic.convert_to_morse(request.form.get("text"))
            return render_template("index2.html", form=TextForm(), text=text)
        else:
            text = logic.convert_to_text(request.form.get("text"))
            return render_template("index2.html", form=TextForm(), text=text)


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
