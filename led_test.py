from machine import Pin
import time

# Test multiple pins with LEDs
# Connect LEDs with 220Ω resistors to these GPIO pins
led_pins = [Pin(i, Pin.OUT) for i in [2, 3, 4, 5, 6, 7]]

print("LED Test Circuit - Knight Rider Pattern")
print("Connect LEDs to GPIO pins 2, 3, 4, 5, 6, 7")
print("Press Ctrl+C to stop")
print("")

try:
    while True:
        # Forward sweep
        for pin in led_pins:
            pin.on()
            time.sleep(0.1)
            pin.off()

        # Reverse sweep
        for pin in reversed(led_pins):
            pin.on()
            time.sleep(0.1)
            pin.off()

except KeyboardInterrupt:
    print("\nTest stopped by user")
    # Turn off all LEDs
    for pin in led_pins:
        pin.off()