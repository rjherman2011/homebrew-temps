from flask import Flask, jsonify, render_template, send_from_directory
from time import strftime
from lib.fileHelper import get_temps
app = Flask(__name__)

#index page. Base of app. Return html
@app.route('/')
def index():
    return render_template('index.html')

#API endpoint
@app.route('/temps/<int:hours>', methods=['GET'])
def return_temps(hours):
    lines = get_temps(hours)
    jsonData = []
    for line in lines:
        items = line.split(',')
        jsonData.append({
            'timeStamp': items[0],
            'outTemp': items[1],
            'inTemp': items[2]
        })

    return jsonify({'loggedTemps' : jsonData})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
