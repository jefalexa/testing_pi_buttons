import RPi.GPIO as GPIO
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.cleanup( (11, 12) )

button1 = 11
button2 = 12

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(button1) == 0:
        print("button1 up")
    if GPIO.input(button2) == 0:
        print("button2 up")
    time.sleep(0.1)


GPIO.cleanup( (11, 12) )
