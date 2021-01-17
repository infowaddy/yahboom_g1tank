import cv2
import time

class VideoStream():
    def gen_frames(self):  
        try:
            camera = cv2.VideoCapture(0)  
            # camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            # camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            # print('cameral resolution is {0} x {1}'.format(camera.get(cv2.CAP_PROP_FRAME_WIDTH), camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))         
            while True:
                success, frame = camera.read()  # read the camera frame 
                if not success:
                    break
                else:
                    ret, buffer = cv2.imencode('.jpg', frame) 
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        except Exception as ex:
            print(ex.__context__)
        finally:
            camera.release()
            time.sleep(0.05)
            cv2.destroyAllWindows()
