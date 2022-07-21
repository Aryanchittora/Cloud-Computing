from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['post'])
def data():
    operation = request.form['operation']
    solve = request.form['text']
    data = requests.get(f'https://newton.now.sh/api/v2//{operation}/{solve}').json()
    result = data['result']

    return render_template('index.html', equation=solve, result=result)

if __name__ == '__main__':
    app.run()