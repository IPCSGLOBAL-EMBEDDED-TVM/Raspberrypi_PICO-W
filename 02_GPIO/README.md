# 02 - GPIO Programming

## Overview
This section covers General Purpose Input/Output (GPIO) programming
using MicroPython on Raspberry Pi Pico W.

## Topics Covered
1. Digital output
2. Digital input
3. Internal pull-up configuration
4. GPIO toggle
5. Multiple LED patterns
6. Button debouncing
7. GPIO interrupts
8. Input-controlled output

## Pin Allocation

| GPIO | Purpose |
|---|---|
| GP2 | LED output |
| GP3 | LED output |
| GP4 | LED output |
| GP14 | Push button input |

## Hardware Requirements
- Raspberry Pi Pico W
- LEDs
- 220-330 ohm resistors
- Push buttons
- Breadboard and jumper wires

## Important
Raspberry Pi Pico W GPIO pins operate at 3.3V logic.
GPIO pins are not 5V tolerant.

## Experiments
Each experiment has its own folder containing:
- `main.py` - MicroPython source code
- `README.md` - Experiment explanation and wiring details
