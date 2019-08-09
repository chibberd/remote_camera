import time
from picamera import PiCamera
import gpiozero
import flask
import uuid
import threading

app = flask.Flask(__name__)


def worker():
    pir = gpiozero.DigitalInputDevice(5)
    counter = 1
    while True:
        pir.wait_for_active
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.capture('static/image_{:d}.jpg'.format(counter))
        camera.close()
        counter += 1
        time.sleep(10)
    return

t = threading.Thread(target=worker)
t.start()


@app.route('/')
def image():
   
    return flask.render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
    t.stop()