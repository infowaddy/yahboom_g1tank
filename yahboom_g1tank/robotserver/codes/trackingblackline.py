import RPi.GPIO as GPIO
import time
from codes.cardrive import CarDrive
from codes.colorled import ColorLED
import multiprocessing

global proc_followline

class TrackingBlackLine():
    def __init__(self, LeftPin1 = 3, LeftPin2 = 5, RightPin1=4, RightPin2 = 18):
        # assign to local variables
        #TrackSensorLeftPin1 TrackSensorLeftPin2 TrackSensorRightPin1 TrackSensorRightPin2
        #      3                 5                  4                   18
        self.TrackSensorLeftPin1  =  LeftPin1   #The first tracking infrared sensor pin on the left is connected to  BCM port 3 of Raspberry pi
        self.TrackSensorLeftPin2  =  LeftPin2   #The second tracking infrared sensor pin on the left is connected to  BCM port 5 of Raspberry pi
        self.TrackSensorRightPin1 =  RightPin1    #The first tracking infrared sensor pin on the right is connected to  BCM port 4 of Raspberry pi
        self.TrackSensorRightPin2 =  RightPin2   #The second tracking infrared sensor pin on the right is connected to  BCMport 18 of Raspberry pi

        #Set the GPIO port to BCM encoding mode.
        GPIO.setmode(GPIO.BCM)

        # Ignore warning information
        GPIO.setwarnings(False)
        
        # Track sensor module pins are initialized into input mode
        GPIO.setup(self.TrackSensorLeftPin1,GPIO.IN)
        GPIO.setup(self.TrackSensorLeftPin2,GPIO.IN)
        GPIO.setup(self.TrackSensorRightPin1,GPIO.IN)
        GPIO.setup(self.TrackSensorRightPin2,GPIO.IN)
        

    # The try/except statement is used to detect errors in the try block.
    # the except statement catches the exception information and processes it.
    def followline(self): 
        try:
            while True:
                # When the black line is detected, the corresponding indicator 
                # of the tracking module is on, and the port level is LOW.
                # When the black line is not detected, the corresponding indicator 
                # of the tracking module is off, and the port level is HIGH.
                TrackSensorLeftValue1  = GPIO.input(self.TrackSensorLeftPin1)
                TrackSensorLeftValue2  = GPIO.input(self.TrackSensorLeftPin2)
                TrackSensorRightValue1 = GPIO.input(self.TrackSensorRightPin1)
                TrackSensorRightValue2 = GPIO.input(self.TrackSensorRightPin2)
                
                # Brake, if all 4 channels cannot deect black line
                # 1 1 1 1
                if (
                    TrackSensorLeftValue1 == True and 
                    TrackSensorLeftValue2 == True and
                    TrackSensorRightValue1 == True and
                    TrackSensorRightValue2 == True
                    ):
                    codes.cardrive.brake
                # go forward, if L2 & R1 can detect black line
                # x 0 0 x
                elif (
                    TrackSensorLeftValue2 == False and
                    TrackSensorRightValue1 == False
                    ):
                    codes.cardrive.forward(0.03, 20)
                # close left, if R1 cannot detect black line
                # and L2 still can detect black line
                # x 0 1 x
                elif (
                    TrackSensorLeftValue2 == False and
                    TrackSensorRightValue1 == True
                    ):
                    codes.cardrive.turnleft(0.03,20)
                # turn left, if L1 can detect black line
                # 0 x x x
                elif TrackSensorLeftValue1 == False:
                    codes.cardrive.spinleft(0.03,25,25)
                # close right, if L1 cannot detect black line
                # and R2 still can detect black line
                # x 1 0 x
                elif (
                    TrackSensorLeftValue2 == True and
                    TrackSensorRightValue1 == False
                    ):
                    codes.cardrive.turnright(0.03,20)
                # turn right, if R2 can detect black line
                # x x x 0
                elif TrackSensorRightValue2 == False:
                    codes.cardrive.spinright(0.03,25,25)
            time.sleep(0.05)
        except KeyboardInterrupt:
            pass

    def start(self):
        global proc_followline
        if not proc_followline.is_alive():
            proc_followline = multiprocessing.Process(name='following_black', target=self.followline)
            proc_followline.start()
        else:
            print("Process is in running...")


    def stop(self):
        global proc_followline
        if proc_followline.is_alive():
            proc_followline.terminate()
            print("process is running, therefore we kill")
        else:
            print("process is not running, therefore nothing to do")


