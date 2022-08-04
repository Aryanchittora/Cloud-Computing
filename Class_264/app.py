# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

# Write load_form function below to Open and redirect to default upload webpage
@app.route('/')
def load():
    return render_template('index.html')

# Write upload_image Function to upload image and redirect to new webpage
@app.route('/gray', methods=['post'])
def upload():
    operation = request.form['input_data']
    file = request.files['file']
    filename = secure_filename(file.filename)
    read_file = file.read()
    img_arr = np.fromstring(read_file, dtype='uint8')
    decode_arr = cv2.imdecode(img_arr, cv2.IMREAD_UNCHANGED)

    if operation == 'gray':
        data = greyscale(decode_arr)
    elif operation == 'sketch':
        data = sketch(decode_arr)
    else:
        print('Invalid Image')
    
    with open(os.path.join('static/', filename), 'wb') as f:
        f.write(data)
    
    message = "Image Uploaded !"

    return render_template('index.html', message=message, filename=filename)

def greyscale(decode_arr):
    # Converting into greyscale
    convert = cv2.cvtColor(decode_arr, cv2.COLOR_RGB2GRAY)
    status, output = cv2.imencode('.PNG', convert)
    print('Status -', status)

    return output

def sketch(decode_arr):
    grey_img = cv2.cvtColor(decode_arr, cv2.COLOR_RGB2GRAY)
    sharp_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(sharp_img, (111, 111), 0)
    sharp_blur = cv2.bitwise_not(blur_img)
    sketch_img = cv2.divide(grey_img, sharp_blur, scale=256.0)
    status, output = cv2.imencode('.PNG', sketch_img)
    print(status)

    return output

# Write display_image Function to display the uploaded image
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()