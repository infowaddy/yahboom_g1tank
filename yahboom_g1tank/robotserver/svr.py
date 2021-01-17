from flask import Flask, flash, render_template, Response, jsonify
from flask_restplus import Api, Resource

from codes.colorled import ColorLED
from codes.servomotors import ServoMotors
from codes.cardrive import CarDrive
import codes.trackingblackline

flask_app = Flask(__name__)
api = Api(flask_app,
            version = "1.0", 
		    title = "Robot API", 
		    description = "YAHBOOM G1 Tank robot Raspberry PI expansion board GPIO control's API")

# define API namespace
led_api = api.namespace('rgbled', description='Front RGB LEDs')
servo_motor_api = api.namespace('servomotors', description='Camera and Ultrasonic motors control')
drive_motor_api = api.namespace('drivingmotors', description = 'Car driving motors control')
channel_tracker_api = api.namespace('chaneltracker', description = '4 Channel infrared black line tracker')


@led_api.route('/blinkon/')
class blinkon(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.blinkon()
        return {
            "status": "LED is blinking."
        }    

@led_api.route('/blinkoff/')
class blinkon(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.blinkoff()
        return {
            "status": "LED is blinking off."
        } 

@led_api.route('/ledon/')
class ledon(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.ledon()
        return { 
            'status': 'LED is switch on.'
        }

@led_api.route('/ledoff/')
class ledoff(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.ledoff()
        return {
            'status': 'LED is switch off.'
        }

@led_api.route('/redon/')
class redon(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.red_on()
        return {
            'status':'Red LED is switch on.'
        }

@led_api.route('/redoff/')
class redoff(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.red_off()
        return {
            'status': 'Red LED is switch off.'
        }

@led_api.route('/greenon/')
class greenon(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.green_on()
        return {
            'status':'Green LED is switch on.'
        }

@led_api.route('/greenoff/')
class greenoff(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.green_off()
        return {
            'status':'Green LED is switch off.'
        }

@led_api.route('/blueon/')
class blueon(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.blue_on()
        return {
            'status':'Blue LED is switch on.'
        }

@led_api.route('/blueoff/')
class blueoff(Resource):
    def get(self):
        colorled = ColorLED()
        colorled.blue_off()
        return {
            'status':'Blue LED is switch off.'
        }

@servo_motor_api.doc(responses={ 200: 'OK'}, params={ 'degree': 'Horizontal degree max = 180, min = 0' })
@servo_motor_api.route('/ultrasonic/<int:degree>')
class ultrasonic(Resource):
    def get(self, degree):
        servomotors = ServoMotors()
        servomotors.servo1_turn(degree)
        return {
            'status':'Ultrasonic motor is in {} degree.'.format(degree)
        }

@servo_motor_api.doc(responses={ 200: 'OK'}, params={ 'degree': 'Horizontal degree max = 180, min = 0' })
@servo_motor_api.route('/camerahorizontal/<int:degree>')
class camerahorizontal(Resource):
    def get(self, degree):
        servomotors = ServoMotors()
        servomotors.servo2_turn(degree)
        return {
            'status':'Camera horizontor motor is in {} degree.'.format(degree)
        }

@servo_motor_api.doc(responses={ 200: 'OK'}, params={ 'degree': 'Vertical degree max = 180, min = 0' })
@servo_motor_api.route('/cameravertical/<int:degree>')
class cameravertical(Resource):
    def get(self, degree):
        servomotors = ServoMotors()
        servomotors.servo3_turn(degree)
        return {
            'status':'Camera vertical motor is in {} degree.'.format(degree)
        }

@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Forward speed max = 180, min =0' })
@drive_motor_api.route('/forward/<int:speed>')
class forward(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.forward(speed)
        cardrive.stop()
        return {
            'status':'Car moved forward.'
        }

@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Backward speed max = 180, min =0' })
@drive_motor_api.route('/backward/<int:speed>')
class backward(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.backward(speed)
        cardrive.stop()
        return {
            'status':'Car moved backward.'
        }

@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Spinning speed max = 180, min =0' })
@drive_motor_api.route('/spinleft/<int:speed>')
class spinleft(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.spinleft(speed)
        cardrive.stop()   
        return {
            'status':'Car spin left.'
        }

@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Spinning speed max = 180, min =0' })
@drive_motor_api.route('/spinright/<int:speed>')
class spinright(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.spinright(speed)
        cardrive.stop()   
        return {
            'status':'Car spin right.'
        }
        
@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Turrning speed max = 180, min =0' })
@drive_motor_api.route('/turnleft/<int:speed>')
class turnleft(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.turnleft(speed)
        cardrive.stop()   
        return {
            'status':'Car turn left.'
        }
        
@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Turrning speed max = 180, min =0' })
@drive_motor_api.route('/turnright/<int:speed>')
class turnright(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.turnright(speed)
        cardrive.stop()   
        return {
            'status':'Car turn right.'
        }

@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Turrning speed max = 180, min =0' })
@drive_motor_api.route('/turnleftblack/<int:speed>')
class turnleftback(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.turnleftback(speed)
        cardrive.stop()   
        return {
            'status':'Car turn left back.'
        }

@drive_motor_api.doc(responses={ 200: 'OK'}, params={ 'speed': 'Turrning speed max = 180, min =0' })
@drive_motor_api.route('/turnrightblack/<int:speed>')
class turnrightback(Resource):
    def get(self, speed):
        cardrive= CarDrive()
        cardrive.turnrightback(speed)
        cardrive.stop()   
        return {
            'status':'Car turn left back.'
        }



def turnrightback():
    cardrive= CarDrive()
    cardrive.turnrightback(50)
    cardrive.stop()
    return 'Car turn right.'


@channel_tracker_api.route('/startfollowline/')
class startfollowline(Resource):
    def get(self):
        codes.trackingblackline.start()
        return {
            'status':'Car is start following black line.'
        }

@channel_tracker_api.route('/stopfollowline/')
class stopfollowline(Resource):
    def get(self):
        codes.trackingblackline.stop()
        return {
            'status':'Car is stopped following black line.'
        }


def video_feed():
    return Response(codes.videostream.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port='5001')
    