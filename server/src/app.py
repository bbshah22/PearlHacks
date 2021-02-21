from flask import Flask, render_template, make_response, request
import os
import time

app = Flask(__name__)

# def format_server_time():
#   server_time = time.localtime()
#   return time.strftime("%I:%M:%S %p", server_time)

# @app.route('/')
# def index():
#     context = { 'server_time': format_server_time() }
#     return render_template('index.html', context=context)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/goals')
def goals():
    return render_template("goals.html")

def workingHours(hour):
  send_to_db = hour
  return render_template("goals.html", time = send_to_db)

@app.route('/goals', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return workingHours(int (text))

@app.route('/buddies')
def buddies():
    return render_template("buddies.html")

@app.route('/buddies_personal')
def buddiesPersonal():
    return render_template("buddies_personal.html")

@app.route('/check_in')
def check_in():
    return render_template("check_in.html")

@app.route('/notific_log')
def notific_log():
    return render_template("notific_log.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))