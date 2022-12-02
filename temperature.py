#! /bin/python

from sense_hat import SenseHat
from flask import Flask

sen= SenseHat()
app = Flask(__name__)

@app.route('/temp', methods={'GET'})
def temp():
    return f"Temperature:{sen.temperature:.2f}, Humidity:{sen.humidity:.2f}"

if __name__ == "__main__":
        app.run(host="127.0.1.1", port=5000)