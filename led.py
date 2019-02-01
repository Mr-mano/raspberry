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

#On dit à la pin GPIO 14 d'arrêter d'envoyer du courant.
lever = 100

#GPIO.output(16, GPIO.LOW)
#GPIO.output(16, GPIO.HIGH)

while (lever != 0):
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    
    time.sleep(0.05)
    
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
  
    time.sleep(0.05)
    
    #lever = lever - 1
    #print("lever =", lever)


#On indique qu'on a fini d'utiliser les GPIOs
GPIO.cleanup()
