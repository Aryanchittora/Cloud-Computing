# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Write load_form function below to Open and redirect to default upload webpage
@app.route('/')
def load():
    return render_template('index.html')

# Write upload_image Function to upload image and redirect to new webpage
@app.route('/gray', methods=['post'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))
    
    message = "Image Uploaded !"

    return render_template('index.html', message=message, filename=filename)

# Write display_image Function to display the uploaded image
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()