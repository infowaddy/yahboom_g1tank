# Import libraries
import RPi.GPIO as GPIO
import time

class ServoMotors():
    # class initiation with servo motor pins with input parameters
    # default GPIO PINs are targeting for Yahboom G1 Tank Expansion Card
    # J1(23) for Ultrasonic, J2(11) for Camera Horizontal, J3(9) for CAmera Vertical
    def __init__(self,
        J1 = 23, J2 = 11, J3 = 9):
        # assign to local veriables
        self.ServoPin1 = J1  # J1 for ultrasonic
        self.ServoPin2 = J2  # J2 for camera horizonal panning
        self.ServoPin3 = J3  # J3 for camera vertical panning

        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BCM)

        # Ignore warning information
        GPIO.setwarnings(False)

        # Set Servo PINs as GPIO out 
        GPIO.setup(self.ServoPin1, GPIO.OUT)
        GPIO.setup(self.ServoPin2, GPIO.OUT)
        GPIO.setup(self.ServoPin3, GPIO.OUT)

        # Create servo objects with 50 Hz frequency as default 
        self.servo1 = GPIO.PWM(self.ServoPin1, 50)
        self.servo2 = GPIO.PWM(self.ServoPin2, 50)
        self.servo3 = GPIO.PWM(self.ServoPin3, 50)
        # Start PWM running, with value of 0 (pulse off)
        self.servo1.start(0)
        self.servo2.start(0)
        self.servo3.start(0)       


    def servo1_turn(self, angle):
        # print("user input angle is {0}".format(angle))
        duty1 = 2+(angle/18)
        # print("calculated duty is {0}".format(duty1))
        self.servo1.ChangeDutyCycle(duty1)
        time.sleep(0.5)
        self.servo1.ChangeDutyCycle(0)
        self.servo1.stop()


    def servo2_turn(self, angle):
        # Start PWM running, with value of 0 (pulse off)
        self.servo2.start(0)
        # print("user input angle is {0}".format(angle))
        duty2 = 2+(angle/18)
        # print("calculated duty is {0}".format(duty2))
        self.servo2.ChangeDutyCycle(duty2)
        time.sleep(0.5)
        self.servo2.ChangeDutyCycle(0)
        self.servo2.stop() 


    def servo3_turn(self, angle):
        # print("user input angle is {0}".format(angle))
        duty3 = 2+(angle/18)
        # print("calculated duty is {0}".format(duty3))
        self.servo3.ChangeDutyCycle(duty3)
        time.sleep(0.5)
        self.servo3.ChangeDutyCycle(0)
        self.servo3.stop()
