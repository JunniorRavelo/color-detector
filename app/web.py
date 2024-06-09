from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

# Define color ranges in HSV
colors = {
    "Red": ([0, 100, 100], [10, 255, 255]),            
    "Red": ([160, 100, 100], [180, 255, 255]),        
    "Orange": ([10, 100, 100], [20, 255, 255]),       
    "Yellow": ([15, 100, 100], [35, 255, 255]),      
    "Green": ([40, 100, 100], [80, 255, 255]),         
    "Blue": ([90, 100, 100], [130, 255, 255]),          
    "Violet": ([120, 100, 100], [160, 255, 255])
    #,"White": ([0, 0, 200], [180, 20, 255]),            
    #"Black": ([0, 0, 0], [180, 255, 30])              
}

colors_high = {
    "Red": ([0, 100, 100], [10, 255, 255]),
    "Dark Red": ([0, 50, 50], [10, 255, 255]),
    "Light Red": ([0, 100, 100], [10, 200, 255]),
    "Pale Red": ([0, 50, 100], [10, 150, 255]),
    "Blue": ([100, 100, 100], [130, 255, 255]),
    "Dark Blue": ([100, 50, 50], [130, 255, 255]),
    "Light Blue": ([100, 100, 100], [130, 200, 255]),
    "Pale Blue": ([100, 50, 100], [130, 150, 255]),
    "Yellow": ([20, 100, 100], [30, 255, 255]),
    "Dark Yellow": ([20, 50, 50], [30, 255, 255]),
    "Light Yellow": ([20, 100, 100], [30, 200, 255]),
    "Pale Yellow": ([20, 50, 100], [30, 150, 255]),
    "Green": ([50, 100, 100], [70, 255, 255]),
    "Dark Green": ([50, 50, 50], [70, 255, 255]),
    "Light Green": ([50, 100, 100], [70, 200, 255]),
    "Pale Green": ([50, 50, 100], [70, 150, 255]),
    "Orange": ([10, 100, 100], [20, 255, 255]),
    "Dark Orange": ([10, 50, 50], [20, 255, 255]),
    "Light Orange": ([10, 100, 100], [20, 200, 255]),
    "Pale Orange": ([10, 50, 100], [20, 150, 255]),
    "Violet": ([130, 100, 100], [160, 255, 255]),
    "Dark Violet": ([130, 50, 50], [160, 255, 255]),
    "Light Violet": ([130, 100, 100], [160, 200, 255]),
    "Pale Violet": ([130, 50, 100], [160, 150, 255]),
    "Yellowish Orange": ([15, 100, 100], [25, 255, 255]),
    "Dark Yellowish Orange": ([15, 50, 50], [25, 255, 255]),
    "Light Yellowish Orange": ([15, 100, 100], [25, 200, 255]),
    "Pale Yellowish Orange": ([15, 50, 100], [25, 150, 255]),
    "Orangeish Red": ([5, 100, 100], [15, 255, 255]),
    "Dark Orangeish Red": ([5, 50, 50], [15, 255, 255]),
    "Light Orangeish Red": ([5, 100, 100], [15, 200, 255]),
    "Pale Orangeish Red": ([5, 50, 100], [15, 150, 255]),
    "Reddish Violet": ([160, 100, 100], [180, 255, 255]),
    "Dark Reddish Violet": ([160, 50, 50], [180, 255, 255]),
    "Light Reddish Violet": ([160, 100, 100], [180, 200, 255]),
    "Pale Reddish Violet": ([160, 50, 100], [180, 150, 255]),
    "Violetish Blue": ([130, 100, 100], [145, 255, 255]),
    "Dark Violetish Blue": ([130, 50, 50], [145, 255, 255]),
    "Light Violetish Blue": ([130, 100, 100], [145, 200, 255]),
    "Pale Violetish Blue": ([130, 50, 100], [145, 150, 255]),
    "Greenish Blue": ([80, 100, 100], [100, 255, 255]),
    "Dark Greenish Blue": ([80, 50, 50], [100, 255, 255]),
    "Light Greenish Blue": ([80, 100, 100], [100, 200, 255]),
    "Pale Greenish Blue": ([80, 50, 100], [100, 150, 255]),
    "Yellowish Green": ([25, 100, 100], [35, 255, 255]),
    "Dark Yellowish Green": ([25, 50, 50], [35, 255, 255]),
    "Light Yellowish Green": ([25, 100, 100], [35, 200, 255]),
    "Pale Yellowish Green": ([25, 50, 100], [35, 150, 255]),
    "White": ([0, 0, 200], [180, 20, 255]),
    "Dark White": ([0, 0, 100], [180, 20, 255]),
    "Light White": ([0, 0, 200], [180, 20, 200]),
    "Pale White": ([0, 0, 100], [180, 20, 200]),
    "Black": ([0, 0, 0], [180, 255, 30]),
    "Dark Black": ([0, 0, 0], [180, 255, 100]),
    "Light Black": ([0, 0, 0], [180, 255, 200]),
    "Pale Black": ([0, 0, 0], [180, 255, 150]),
}

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for color, (lower, upper) in colors.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filter small contours by area
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
    return frame

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = detect_color(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)