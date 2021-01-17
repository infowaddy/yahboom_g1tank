# import python modules
import RPi.GPIO as GPIO # for GPIO - General Purpose Input Output Pin of Raspberry PI
import time # for sleep

# set default PWM pin frequency to 50HZ
global Freeqz
Freeqz = 50

class CarDrive():
    # class initiation with motor pins with input parameters
    # default GPIO PINs are targeting for Yahboom G1 Tank Expansion Card
    def __init__(self, 
        LeftMotorPIN1 = 20, LeftMotorPIN2 = 21, LeftMotorEnablePIN = 16,
        RightMotorPIN1 = 19, RightMotorPIN2 = 26, RightMotorEnablePIN = 13):
        # assign to local variables
        self.LIN1 = LeftMotorPIN1
        self.LIN2 = LeftMotorPIN2
        self.LEA = LeftMotorEnablePIN
        self.RIN1 = RightMotorPIN1
        self.RIN2 = RightMotorPIN2
        self.REA = RightMotorEnablePIN
        # set the GPIO port to BCM encoding mode
        GPIO.setmode(GPIO.BCM)
        # ignore warning information
        GPIO.setwarnings(False)
        # pwm pins set as out with high volt
        GPIO.setup(self.LEA, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.REA, GPIO.OUT, initial=GPIO.HIGH)
        # motors pins set as out with low volt
        GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.LOW)
        # set pwm frequency  
        self.PWM_LEA = GPIO.PWM(self.LEA, Freeqz)
        self.PWM_REA = GPIO.PWM(self.REA, Freeqz)
        # set pwm duty cycle as zero, let mortor in stop condition
        self.PWM_LEA.start(0)
        self.PWM_REA .start(0)

    
    # generic drive method    
    def drive(self, speed = 20, backward = 0, left_turn = 0, right_turn = 0, spin = True, sleep = 0):
        # speed value is max 100 and min 0
        if (speed > 100): speed = 100
        elif (speed < 0): leftSpeed = 0        

        # set same speed of left and right motor
        self.PWM_LEA.ChangeDutyCycle(abs(speed))
        self.PWM_REA.ChangeDutyCycle(abs(speed))

        # for forward drive
        if (backward == 0 and left_turn == 0 and right_turn == 0):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.LOW)

        # for backward drive
        elif (backward == 1 and left_turn == 0 and right_turn == 0):
            print("backward")
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.HIGH)

        # for turn left forward
        elif (backward == 0 and left_turn == 1 and right_turn == 0 and spin == False):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.LOW)
        
        # for turn right forward
        elif (backward == 0 and left_turn == 0 and right_turn == 1 and spin == False):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.LOW)

         # for turn left backward
        elif (backward == 1 and left_turn == 1 and right_turn == 0 and spin == False):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.LOW)
        
        # for turn right backward
        elif (backward == 1 and left_turn == 0 and right_turn == 1 and spin == False):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.HIGH)

        # for spin left in same place
        elif (backward == 0 and left_turn == 1 and right_turn == 0 and spin == True):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.LOW)
        
        # for spin right in same place
        elif (backward == 0 and left_turn == 0 and right_turn == 1 and spin == True):
            GPIO.setup(self.LIN1, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.LIN2, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN1, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self.RIN2, GPIO.OUT, initial=GPIO.HIGH)
        
        time.sleep(sleep)

    
    # backward
    def backward(self, speed = 20, duration = 0.3):
        try:
            self.drive(speed, 1, 0, 0, True, 0.05)
            time.sleep(duration)
        except KeyboardInterrupt:
            pass
    
    # forward
    def forward(self, speed = 20, duration = 0.3):
        try:
            self.drive(speed, 0, 0, 0, True, duration)
        except KeyboardInterrupt:
            pass

    # spin left 
    def spinleft(self, speed = 20, duration = 0.3):
        try:            
            self.drive(speed, 0, 1, 0, True, duration)
        except KeyboardInterrupt:
            pass
    
    # spin right
    def spinright(self, speed = 20, duration = 0.3):
        try:
            self.drive(speed, 0, 0, 1, True, duration)
        except KeyboardInterrupt:
            pass

    # turn left forward
    def turnleft(self, speed = 20, duration = 0.3):
        try:            
            self.drive(speed, 0, 1, 0, False, duration)
        except KeyboardInterrupt:
            pass
    
    # turn right forward
    def turnright(self, speed = 20, duration = 0.3):
        try:
            self.drive(speed, 0, 0, 1, False, duration)
        except KeyboardInterrupt:
            pass

    # turn left backward
    def turnleftback(self, speed = 20, duration = 0.3):
        try:            
            self.drive(speed, 1, 1, 0, False, duration)
        except KeyboardInterrupt:
            pass
    
    # turb right backward
    def turnrightback(self, speed = 20, duration = 0.3):
        try:
            self.drive(speed, 1, 0, 1, False, duration)
        except KeyboardInterrupt:
            pass


    # motor stop and reset GPIO PINS
    def stop(self):
        self.PWM_LEA.ChangeDutyCycle(0)
        self.PWM_REA.ChangeDutyCycle(0)
        GPIO.output(self.LIN1, GPIO.LOW)
        GPIO.output(self.LIN2, GPIO.LOW)
        GPIO.output(self.RIN1, GPIO.LOW)
        GPIO.output(self.RIN2, GPIO.LOW)
    