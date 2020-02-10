#!/usr/bin/python

# Path to pngview (raspidmx)
PNGVIEWPATH = "/home/pi/Desktop/raspidmx-master/pngview"

# Path to icon set
ICONPATH = "icons/medium"

# Show battery icon
ICON = 1

# Set red and green LEDs
LEDS = 0

# Icon location
ICONX = 760
ICONY = 50

# ADC type (MCP3001, MCP3008 or MCP3551)
ADC = "MCP3002"

# ADC channel to use (from 0 to 7, only relevant for MCP3008)
ADCCHANNEL = 0

# ADC SPI pins (BOARD numbering scheme)
SPIMISO = 21
SPIMOSI = 19
SPICLK = 23
SPICS = 24

# GPIO pins for good voltage and low voltage LEDs (BOARD numbering scheme)
GOODVOLTPIN = 18
LOWVOLTPIN = 16

# Fully charged voltage, voltage at the percentage steps and shutdown voltage
VOLT100 = 2.6
VOLT75 = 2.45
VOLT50 = 2.3
VOLT25 = 2.05
VOLT0 = 1.8

# Value (in ohms) of the lower resistor from the voltage divider, connected to the ground line (1 if no voltage divider)
LOWRESVAL = 10000

# Value (in ohms) of the higher resistor from the voltage divider, connected to the positive line (0 if no voltage divider)
HIGHRESVAL = 40000

# ADC voltage reference (3.3V for Raspberry Pi)
ADCVREF = 3.3

# Refresh rate (s)
REFRESHRATE = 1

# Display debug messages
DEBUGMSG = 0

# Create CSV output
CSVOUT = 0
