import pigpio
import time

# GPIO pins
DIR = 27   # Direction
SLP = 23   # Sleep (active high)
STP = 17   # Step

def main():
    pi = pigpio.pi()
    if not pi.connected:
        print("pigpio daemon not running. Start it with: sudo pigpiod")
        return

    # Set pin modes
    pi.set_mode(DIR, pigpio.OUTPUT)
    pi.set_mode(SLP, pigpio.OUTPUT)
    pi.set_mode(STP, pigpio.OUTPUT)

    # Wake up the driver
    pi.write(SLP, 1)
    pi.write(DIR, 0)

    delay = 0.001  # 1 ms pulse (1000 steps/sec)
    steps = 200    # steps per half rotation, adjust as needed

    try:
        while True:
            # Step motor forward
            pi.write(DIR, 0)
            for _ in range(steps):
                pi.write(STP, 1)
                time.sleep(delay)
                pi.write(STP, 0)
                time.sleep(delay)

            # Step motor backward
            pi.write(DIR, 1)
            for _ in range(steps):
                pi.write(STP, 1)
                time.sleep(delay)
                pi.write(STP, 0)
                time.sleep(delay)

    except KeyboardInterrupt:
        pass
    finally:
        # Put driver to sleep and release pigpio
        pi.write(SLP, 0)
        pi.stop()

if __name__ == "__main__":
    main()

