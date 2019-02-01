#import des utilistaires python
import RPi.GPIO as GPIO
import time

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initialisation de la broche en mode "sortie"
#⚠️ Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de la broche.
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/on/')
def on():
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
        
    return render_template('template-on.html')

@app.route('/off/')
def off():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)

    return render_template('template-off.html')
