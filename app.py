from flask import Flask, jsonify
from temperature_sensor import get_current_temperature

app = Flask(__name__)

@app.route('/get-temperature', methods=['GET'])
def get_temperature():
    data = get_current_temperature()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)