from flask import Flask
import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/led/on')
def led_on():
    gp.output(18, gp.HIGH)
    return "<h1>LED ON</h1>"

@app.route('/led/off')
def led_off():
    gp.output(18, gp.LOW)
    return "<h1>LED OFF</h1>"

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
