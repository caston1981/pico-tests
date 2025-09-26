from machine import Pin
import time

# Test pairs: (output_pin, input_pin)
# Connect jumper wires between these pairs for testing
test_pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

print("Hardware Loopback Test")
print("Make sure to connect jumper wires between the pin pairs listed above")
print("")

for out_pin, in_pin in test_pairs:
    print(f"Testing pair: GPIO{out_pin} -> GPIO{in_pin}")

    try:
        output = Pin(out_pin, Pin.OUT)
        input_pin = Pin(in_pin, Pin.IN, Pin.PULL_DOWN)

        # Test HIGH
        output.on()
        time.sleep(0.01)
        if input_pin.value() == 1:
            print(f"  HIGH test: PASS")
        else:
            print(f"  HIGH test: FAIL")

        # Test LOW
        output.off()
        time.sleep(0.01)
        if input_pin.value() == 0:
            print(f"  LOW test: PASS")
        else:
            print(f"  LOW test: FAIL")

    except Exception as e:
        print(f"  Error testing pair: {e}")

    print("")