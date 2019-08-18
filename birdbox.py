import time
from picamera import PiCamera
import gpiozero
import flask
import uuid
import threading
import LIS3DH


app = flask.Flask(__name__)


def read_pir():
    pir = gpiozero.DigitalInputDevice(5)
    pir.value()

def read_accelerometer():
    accel = LIS3DH.Accelerometer('spi', i2cAddress = 0x0, spiPort = 0, spiCS = 0)  # spi connection alternative
    accel.set_ODR(odr=50, powerMode='normal')
    accel.axis_enable(x='on',y='on',z='on')
    accel.interrupt_high_low('high')
    accel.latch_interrupt('on')
    accel.set_BDU('on')
    accel.set_scale()
    x = accel.x_axis_reading()
    y = accel.y_axis_reading()
    z = accel.z_axis_reading()
                   
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