from machine import Pin
import time

# Test all GPIO pins as outputs
pins = []
for i in range(29):  # GP0 to GP28
    try:
        pin = Pin(i, Pin.OUT)
        pins.append((i, pin))
        print(f"GPIO {i}: OK")
    except:
        print(f"GPIO {i}: Failed")

print(f"\nSuccessfully initialized {len(pins)} GPIO pins")

# Blink test
print("\nStarting blink test...")
for gpio_num, pin in pins:
    pin.on()
    time.sleep(0.1)
    pin.off()

print("Blink test complete.")