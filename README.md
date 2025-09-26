# Raspberry Pi Pico GPIO Testing Suite

This project provides comprehensive testing tools for Raspberry Pi Pico GPIO headers from Ubuntu Linux.

## Prerequisites

- Raspberry Pi Pico
- USB cable
- Ubuntu Linux system
- MicroPython firmware for Pico (download from raspberrypi.org)

## Setup

1. Run the setup script to install required tools:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. Flash MicroPython firmware to your Pico:
   - Download the latest MicroPython UF2 file from raspberrypi.org
   - Put Pico into bootloader mode (hold BOOTSEL while plugging in)
   - Copy the UF2 file to the RPI-RP2 drive

## Testing Methods

### 1. Basic Connectivity Test
```bash
chmod +x connectivity_test.sh
./connectivity_test.sh
```
This checks if your Pico is properly recognized by the system.

### 2. GPIO Pin Test
Upload `gpio_test.py` to your Pico and run it. This tests all GPIO pins as outputs and performs a blink test.

### 3. Hardware Loopback Test
Upload `loopback_test.py` to your Pico. Connect jumper wires between the specified pin pairs and run the test to verify signal integrity.

### 4. LED Test Circuit
Upload `led_test.py` to your Pico. Connect LEDs with 220Ω resistors to GPIO pins 2-7 and run for a visual "Knight Rider" pattern.

### 5. Multimeter Verification
Use a multimeter to verify:
- GPIO pins read 3.3V when set HIGH
- GPIO pins read 0V when set LOW
- Power rails: 3.3V pin = 3.3V, VBUS = 5V, GND = 0V

## Usage with MicroPython

To upload and run scripts on your Pico:

1. Connect Pico via USB
2. Use rshell:
   ```bash
   rshell -p /dev/ttyACM0
   cp gpio_test.py /pyboard/
   repl
   import gpio_test
   ```

Or use Thonny IDE for a graphical interface.

## Troubleshooting

- If Pico isn't recognized: Check USB cable and try different ports
- If serial connection fails: Ensure MicroPython is flashed and device is `/dev/ttyACM0`
- For GPIO issues: Use loopback test to isolate problematic pins

Start with the connectivity test, then progress to GPIO testing methods.
