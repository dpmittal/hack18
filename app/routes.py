from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method=='POST':
        result = request.form
        return render_template("translate.html", result=result)

@app.errorhandler(404)
def error_handler(e):
    return render_template("404.html")

if __name__ == '__main__':
   app.run(debug = True)
