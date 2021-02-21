from flask import Flask, render_template
# from pyowm import OWM
app = Flask(
    __name__,
    template_folder="templates"
)
app.static_folder = 'static'
# owm = OWM('1dcc5e56f0ad69d652fb00cf0b0c81dd')

@app.route('/')
def home():
    return render_template("test.html")

@app.route('/goals')
def goals():
    return render_template("goals.html")

@app.route('/buddies')
def buddies():
    return render_template("buddies.html")

@app.route('/check_in')
def check_in():
    return render_template("check_in.html")

@app.route('/notific_log')
def notific_log():
    return render_template("notific_log.html")

# @app.route('/weather/<city>')
# def weather(city):
#     return f'It\'s always sunny in {city}' 

# @app.route('/weather/<city>')
# def weather(city):
#     weather_manager = owm.weather_manager()
#     weather_at_place = weather_manager.weather_at_place(f'{city},US')
#     return weather_at_place.weather.temperature('celsius')

# Keep this at the bottom of run.py
app.run(debug=True)