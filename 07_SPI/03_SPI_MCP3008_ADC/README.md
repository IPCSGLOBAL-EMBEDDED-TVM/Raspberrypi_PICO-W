# 03 SPI MCP3008 ADC

## Objective
Read an analog voltage through an MCP3008 SPI ADC.

## Hardware Requirements
- Raspberry Pi Pico W
- Hardware listed in the wiring instructions below

## Wiring
MCP3008 VDD/VREF to 3.3V, AGND/DGND to GND. Connect CLK GP18, DIN GP19, DOUT GP16, CS GP17. CH0 receives a 0-3.3V signal.

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
