from flask import Flask, render_template, request
import model_read

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html', methods=['POST'])
def index1():
    name = request.form['userInput']    
    return render_template('index.html') + model_read.Give_emotion(name)


@app.route('/' ,methods=['POST'])
def hello():
    name = request.form['userInput']
    emotion = "<h1>" + model_read.Give_emotion(name) + "</h1>"
    return emotion

if __name__ == '__main__':
    from waitress import serve
    print("hosting on 8080 port")
    serve(app, host="0.0.0.0", port=8080)
