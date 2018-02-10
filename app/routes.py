from flask import Flask, render_template, url_for, request, redirect
import scraper
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        res = request.form
        scraper.scrape(res)
        return render_template("resc.html")

@app.errorhandler(404)
def error_handler(e):
    return render_template("404.html")

if __name__ == '__main__':
   app.run(debug = True)
