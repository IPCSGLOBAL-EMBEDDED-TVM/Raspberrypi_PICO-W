# 03 - PWM Programming

## Overview
This section introduces Pulse Width Modulation (PWM) using
MicroPython on Raspberry Pi Pico W.

## Topics Covered
1. PWM fundamentals
2. LED brightness control
3. LED fading
4. Passive buzzer control
5. Buzzer tone generation
6. Servo motor control

## Pin Allocation

| GPIO | Purpose |
|---|---|
| GP15 | LED PWM |
| GP16 | Passive buzzer |
| GP17 | Servo signal |

## Hardware Requirements
- Raspberry Pi Pico W
- LED and 220-330 ohm resistor
- Passive piezo buzzer
- Hobby servo motor
- Suitable external servo power supply
- Breadboard and jumper wires

## Important
- PWM controls the average power delivered to a load.
- A passive buzzer can generate different tones using PWM.
- An active buzzer generally needs only an on/off control signal.
- Power the servo from a suitable external supply.
- Connect the external supply ground to Pico W GND.
- Do not power a servo directly from a GPIO pin.

## Experiments
Each experiment has its own folder containing:
- `main.py` - MicroPython source code
- `README.md` - Experiment explanation and wiring details
