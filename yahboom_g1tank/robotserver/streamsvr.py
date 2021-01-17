from flask import Flask, flash, render_template, Response, jsonify
from codes.videostream import VideoStream

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    videostream = VideoStream()    
    return Response(videostream.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')