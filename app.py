from flask import Flask, jsonify
from temperature_sensor import get_current_temperature
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/get-temperature', methods=['GET'])
def get_temperature():
    data = get_current_temperature()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)