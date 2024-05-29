import pandas as pd
from flask import Flask, render_template, request
import suspicious_chat_v2
from symspell_helper import correct_text

app = Flask(__name__)

dataset = pd.read_csv("labeled_data.csv")
suspicious = suspicious_chat_v2.SuspiciousDetection(dataset)
messages = []
outputs = []
corrected_messages = []

@app.route('/', methods=['GET'])
def hello_world():
    suspicious.load_model()
    return render_template('index.html', name="ML", messages=messages, prediction=outputs, corrected_messages=corrected_messages)

@app.route('/', methods=['POST'])
def predict():
    sentence = request.form['message']
    corrected_sentence = correct_text(sentence)  # Metni düzelt
    messages.append(sentence)  # Orijinal metni ekle
    corrected_messages.append(corrected_sentence)  # Düzeltme sonrası metni ekle
    output = suspicious.predict_sentence(corrected_sentence)
    outputs.append(output)
    return render_template('index.html', name="ML", prediction=outputs, messages=messages, corrected_messages=corrected_messages)

if __name__ == '__main__':
    app.run()
