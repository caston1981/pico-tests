#!/bin/bash

# Basic connectivity test for Raspberry Pi Pico

echo "Checking USB devices..."
lsusb | grep -i "raspberry\|pico" || echo "Pico not found in lsusb output"

echo ""
echo "Checking kernel messages..."
dmesg | tail -20 | grep -i "tty\|usb" || echo "No recent USB/tty messages found"

echo ""
echo "Available serial devices:"
ls /dev/tty* 2>/dev/null | grep -E "(ACM|USB)" || echo "No ACM/USB serial devices found"

echo ""
echo "To connect to Pico (if running MicroPython):"
echo "screen /dev/ttyACM0 115200"