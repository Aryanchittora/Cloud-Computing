import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image


app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['post'])
def upload():
    img = request.files['file']
    degree = request.form['degree']
    int_degree = int(degree)
    secure = secure_filename(img.filename)
    img.save(os.path.join('static/', img.filename))
    image_open = Image.open(img)
    rotated = image_open.rotate(int_degree)
    rotated.save(os.path.join('static/', 'rotated.jpg'))
    file_name = 'rotated.jpg'

    return render_template('upload.html', filename=file_name)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='rotated.jpg'))

if __name__ == "__main__":
    app.run()
