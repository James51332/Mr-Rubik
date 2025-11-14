import pigpio
import time

# GPIO pins
ACT = 24  
ARM = 19

def main():
	pi = pigpio.pi()
	if not pi.connected:
		print("pigpio daemon not running. Start it with: sudo pigpiod")
		return

	# Set pin modes
	pi.set_mode(ACT, pigpio.OUTPUT)
	pi.set_mode(ARM, pigpio.OUTPUT)

	angle = 0

	try:
		while True:
			pi.

	except KeyboardInterrupt:
		pass
	finally:
		# Put driver to sleep and release pigpio
		pi.write(SLP, 0)
		pi.stop()

if __name__ == "__main__":
	main()


