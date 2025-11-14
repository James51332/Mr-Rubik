from flask import Flask, Response
from picamera2 import Picamera2
from PIL import Image
import io, numpy as np

app = Flask(__name__)
picam2 = Picamera2()

# Configure for RGB frames
config = picam2.create_preview_configuration(main={"format": "BGR888"})
picam2.configure(config)
picam2.start()

def apply_gamma(image_array, gamma=1.8):
    # Build lookup table once
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in range(256)]).astype("uint8")
    return table[image_array]

def gen_frames():
    while True:
        frame = picam2.capture_array("main")  # RGB888
        corrected = apply_gamma(frame, gamma=1.8)

        # Encode to JPEG
        img = Image.fromarray(corrected)
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        frame_bytes = buf.getvalue()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return """
    <html>
    <body>
        <h1>Camera Stream</h1>
        <img src="/video_feed" width="640" height="480"/>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

