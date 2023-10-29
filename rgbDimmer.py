from time import sleep
import RPi.GPIO as GPIO
delay = .1
blueButtonPin = 36
greenButtonPin = 38
redButtonPin = 40
redLEDpin = 37
greenLEDpin = 35
blueLEDpin = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(blueLEDpin, GPIO.OUT)
GPIO.setup(redLEDpin, GPIO.OUT)
GPIO.setup(greenLEDpin, GPIO.OUT)
GPIO.setup(blueButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

redPWM = GPIO.PWM(redLEDpin, 100)
greenPWM = GPIO.PWM(greenLEDpin, 100)
bluePWM = GPIO.PWM(blueLEDpin, 100)


redButtonState = 1
redButtonStateOld = 1
greenButtonState = 1
greenButtonStateOld = 1
blueButtonState = 1
blueButtonStateOld = 1
redLEDstate = 0
greenLEDstate = 0
blueLEDstate = 0

redBrightness = 0
greenBrightness = 0
blueBrightness = 0

def red():
    global redBrightness
    global redLEDstate
    redLEDstate = not redLEDstate
    if redBrightness < 90:
        redBrightness += 11.11
        redPWM.start(redBrightness)
    else:
        print("Bulb maxed")
        redBrightness = 0
        redPWM.stop()
    print("redBrightness: ", redBrightness)
        
    
def green():
    global greenBrightness
    global greenLEDstate
    greenLEDstate = not greenLEDstate
    if greenBrightness < 90:
        greenBrightness += 11.11
        greenPWM.start(greenBrightness)
    else:
        print("Bulb maxed")
        greenBrightness = 0
        greenPWM.stop()
    print("greenBrightness: ", greenBrightness)
    
def blue():
    global blueBrightness
    global blueLEDstate
    blueLEDstate = not blueLEDstate
    if blueBrightness < 90:
        blueBrightness += 11.11
        bluePWM.start(blueBrightness)
    else:
        print("Bulb maxed")
        blueBrightness = 0
        bluePWM.stop()
    print("blueBrightness: ", blueBrightness)
   
    

if __name__ == "__main__":
    
    try:
        
        while True:
            greenButtonState = GPIO.input(greenButtonPin)
            redButtonState = GPIO.input(redButtonPin)
            blueButtonState = GPIO.input(blueButtonPin)
            #print(buttonStateBright)
            if redButtonState == 0 and redButtonStateOld == 1 :
                red()

            if greenButtonState == 0 and greenButtonStateOld == 1 :
                green()
                
            if blueButtonState == 0 and blueButtonStateOld == 1 :
                blue()
            
            #print("blue button: ", blueButtonState)
            redButtonStateOld = redButtonState
            greenButtonStateOld = greenButtonState
            blueButtonStateOld = blueButtonState
            sleep(delay)
            
           

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("adios")



