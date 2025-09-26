#!/bin/bash

# Setup script for Raspberry Pi Pico development on Ubuntu

echo "Updating package list..."
sudo apt update

echo "Installing build tools..."
sudo apt install -y build-essential cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib

echo "Installing Python tools..."
sudo apt install -y python3-pip screen

echo "Installing Python packages..."
pip3 install esptool rshell

echo "Setup complete. You may also want to install Thonny IDE:"
echo "pip3 install thonny"