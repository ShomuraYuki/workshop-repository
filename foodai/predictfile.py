import os
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

from keras.models import Sequential, load_model
import keras,sys
import numpy as np
import pandas as pd
from PIL import Image

classes = ["cabbage", "carrot", "japaneseradish", "onion", "tomato"]
num_classes = len(classes)
judge = pd.DataFrame([{ 
    "cabbage" : "can",
    "carrot" : "can",
    "japaneseradish" : "can",
    "onion" : "cannot",
    "tomato" : "can"
}])
image_size = 50

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            model = load_model('./food_cnn.h5')

            image = Image.open(filepath)
            image = image.convert('RGB')
            image = image.resize((image_size, image_size))
            data = np.asarray(image)
            X = []
            X.append(data)
            X = np.array(X)

            result = model.predict([X])[0]
            predicted = result.argmax()
            #percentage = int(result[predicted] * 100)

            if judge[classes[predicted]][0] == "can":
                message = "食べても問題ありません。"
            else:
                message = "食べてはいけません。"

            #return "ラベル： " + classes[predicted] + ", 判定： " + message

            return render_template('result.html', message=message, label=classes[predicted] ,img_url=filepath)

            #return "ラベル： " + classes[predicted] + ", 確率："+ str(percentage) + " %"

            #return redirect(url_for('uploaded_file', filename=filename))
    return render_template('home.html')

from flask import send_from_directory

@app.route('/check')
def a():
    return render_template('check.html')

@app.route('/research')
def b():
    return render_template('research.html')

@app.route('/how')
def c():
    return render_template('how.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
