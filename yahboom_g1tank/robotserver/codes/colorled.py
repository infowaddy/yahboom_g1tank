import RPi.GPIO as GPIO
import time
import multiprocessing

global proc_blinkLED

class ColorLED():
    # class initiation with motor pins with input parameters
    # default GPIO PINs are targeting for Yahboom G1 Tank Expansion Card
    def __init__ (self, 
        Red = 22, Green = 27, Blue = 24):
        # assign to local variables
        self.Red = Red
        self.Green = Green
        self.Blue = Blue
        # et the GPIO port to BCM encoding mode.
        GPIO.setmode(GPIO.BCM)
        # set LED PINs as out put pin
        GPIO.setup(self.Red, GPIO.OUT)
        GPIO.setup(self.Green, GPIO.OUT)
        GPIO.setup(self.Blue, GPIO.OUT)
        # set global variable default value
        self.lighton = 0

    def red_on(self):
        GPIO.output(self.Red, GPIO.HIGH)
    
    def red_off(self):
        GPIO.output(self.Red, GPIO.LOW)
    
    def green_on(self):
        GPIO.output(self.Green, GPIO.HIGH)
    
    def green_off(self):
        GPIO.output(self.Green, GPIO.LOW)

    def blue_on(self):
        GPIO.output(self.Blue, GPIO.HIGH)
    
    def blue_off(self):
        GPIO.output(self.Blue, GPIO.LOW)

    def ledon(self):   
        self.red_on()
        self.green_on()
        self.blue_on

    def ledoff(self):
        self.lighton = 0
        self.red_off()
        self.green_off()
        self.blue_off()
        GPIO.cleanup()
        

    def blinkLED(self):
        _sleep = 0.3
        # Display 7 color LED
        try:
            while self.lighton == 1:
                # Red | X | X 
                self.red_on()
                self.green_off()
                self.blue_off()
                time.sleep(_sleep)
                # X | Green | X 
                self.red_off()
                self.green_on()
                self.blue_off()                
                time.sleep(_sleep)
                # X | X | Blue
                self.red_off()
                self.green_off()
                self.blue_on()
                time.sleep(_sleep)
                # Red | Green | X 
                self.red_on()
                self.green_on()
                self.blue_off()
                time.sleep(_sleep)
                # Red | X | Blue 
                self.red_on()
                self.green_off()
                self.blue_on()
                time.sleep(_sleep)
                # X | Green | Blue 
                self.red_off()
                self.green_on()
                self.blue_on()
                time.sleep(_sleep)
                # X | X | X 
                self.red_off()                
                self.green_off()                
                self.blue_off()
                time.sleep(_sleep)
        except Exception as ex:
            print(ex.__context__)
                

    def blinkoff(self):
        print("blink off method")
        self.lighton = 0
        global proc_blinkLED
        if "proc_blinkLED" in globals() and proc_blinkLED.is_alive():
            proc_blinkLED.terminate()
            print("process is running, therefore we kill")


    def blinkon(self):
        self.lighton = 1
        global proc_blinkLED
        print("blink on method")
        
        isstarted = 0
        if "proc_blinkLED" in globals() and proc_blinkLED.is_alive():
            isstarted = 1                
       
        if (isstarted == 0):
            proc_blinkLED = multiprocessing.Process(name='blinking_led', target=self.blinkLED)
            proc_blinkLED.start()
        else:
            print("Process is in running...")

