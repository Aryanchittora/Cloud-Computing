import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')



if __name__ == "__main__":
    app.run(debug=True)
