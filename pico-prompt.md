To test your Raspberry Pi Pico and GPIO headers from Ubuntu, here are several approaches you can use:

## Basic Connectivity Test

First, connect your Pico to your laptop via USB. Check if it's recognized:
```bash
lsusb
dmesg | tail
```

You should see the Pico appear as a USB device.

## Install Development Tools

Install the necessary tools:
```bash
sudo apt update
sudo apt install build-essential cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib
```

For MicroPython (easier option):
```bash
sudo apt install python3-pip
pip3 install esptool rshell thonny
```

## Method 1: MicroPython GPIO Test

1. **Flash MicroPython firmware** to your Pico (download from raspberrypi.org)
2. **Connect via serial console**:
   ```bash
   sudo apt install screen
   screen /dev/ttyACM0 115200
   ```

3. **Test GPIO pins** with this simple script:
   ```python
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
   
   # Blink test
   for gpio_num, pin in pins:
       pin.on()
       time.sleep(0.1)
       pin.off()
   ```

## Method 2: Hardware Loopback Test

For thorough testing, create jumper wire connections between pairs of pins and run a loopback test:

```python
from machine import Pin
import time

# Test pairs: (output_pin, input_pin)
test_pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

for out_pin, in_pin in test_pairs:
    output = Pin(out_pin, Pin.OUT)
    input_pin = Pin(in_pin, Pin.IN, Pin.PULL_DOWN)
    
    # Test HIGH
    output.on()
    time.sleep(0.01)
    if input_pin.value() == 1:
        print(f"GPIO {out_pin}->{in_pin}: HIGH test PASS")
    else:
        print(f"GPIO {out_pin}->{in_pin}: HIGH test FAIL")
    
    # Test LOW
    output.off()
    time.sleep(0.01)
    if input_pin.value() == 0:
        print(f"GPIO {out_pin}->{in_pin}: LOW test PASS")
    else:
        print(f"GPIO {out_pin}->{in_pin}: LOW test FAIL")
```

## Method 3: LED Test Circuit

Connect LEDs with current-limiting resistors (220Ω) to multiple GPIO pins and run:

```python
from machine import Pin
import time

# Test multiple pins with LEDs
led_pins = [Pin(i, Pin.OUT) for i in [2, 3, 4, 5, 6, 7]]

# Knight Rider pattern
while True:
    for pin in led_pins:
        pin.on()
        time.sleep(0.1)
        pin.off()
    for pin in reversed(led_pins):
        pin.on()
        time.sleep(0.1)
        pin.off()
```

## Method 4: Multimeter Verification

Use a multimeter to verify voltage levels:
- Set GPIO pins HIGH in software and measure 3.3V
- Set GPIO pins LOW and measure 0V
- Test all pins systematically

## Power Supply Test

Verify the power rails:
- 3.3V pin should read 3.3V
- 5V pin (VBUS) should read 5V when USB connected
- GND pins should be 0V

Start with the MicroPython approach as it's the quickest way to verify basic functionality. If you encounter issues with specific pins, use the hardware loopback method to isolate problems.