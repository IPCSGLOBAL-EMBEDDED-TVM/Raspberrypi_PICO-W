# 07 ADC Threshold Control

## Objective
Switch an LED when an analog input crosses a threshold.

## Hardware Requirements
- Raspberry Pi Pico W
- Hardware listed in the wiring instructions below

## Wiring
Potentiometer wiper to GP26; outer terminals to 3V3/GND. LED on GP15 through a 220-330 ohm resistor.

## Source Code
See `main.py`.

## How to Run
1. Connect the Pico W to your computer.
2. Open the project in Thonny or your MicroPython-compatible editor.
3. Upload `main.py` to the Pico W.
4. Run the program.
5. Observe the output in the serial terminal or on the connected hardware.

## Learning Outcomes
- Understand the peripheral or protocol used in this experiment.
- Configure the relevant MicroPython interface.
- Observe the hardware response or serial output.
- Modify the program to explore different configurations.

## Safety Notes
- Pico W GPIO and ADC inputs use 3.3V logic.
- Do not apply 5V to GPIO or ADC pins.
- Check the connected module's voltage requirements.
- Use common ground for external circuits.
