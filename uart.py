#!/usr/bin/env python3

# IMPORTANT: remember to add "enable_uart=1" line to /boot/config.txt

from gpiozero import OutputDevice
from time import sleep
#from serial import Serial
import serial

# RO  <-> GPIO15/RXD
# RE  <-> GPIO17
# DE  <-> GPIO27
# DI  <-> GPIO14/TXD

# VCC <-> 3.3V
# B   <-> RS-485 B
# A   <-> RS-485 A
# GND <-> GND

re = OutputDevice(17)
de = OutputDevice(27)

message = bytearray(b'\xfb\x00')
# append addrss
#   0x0E
#   E: receiver address, 14 int
#   D: sender address, 13 int
message.append(int("0x0e", 16))

# Reading the device version (0x0A)
message.append(int("0x0a", 16))

# CRC
# TODO CRC function
# 0x67B5
message.append(int("0x67", 16))
message.append(int("0xB5", 16))


# data end
message.append(int("0xBF", 16))

for i in range(0, len(message)):
    print('print message: 0x%02x' % message[i])


SERIAL_PORT = '/dev/serial0'
BAUD_RATES = 115200
ser = serial.Serial(SERIAL_PORT, BAUD_RATES)

# enable transmission mode
de.on()
re.on()
print('writing message')
ser.write(message)
ser.flush()

sleep(0.1)

# enable reception mode
de.off()
re.off()
print('reading message')
rx = ser.read(1024)
print(rx)

print('done')


exit()
#with Serial('/dev/serial0', 115200) as s:
#    # enable transmission mode
#    de.on()
#    re.on()
#    print('writing message')
#    s.write(message)
#    s.flush()
#
#    # wait some time before echoing
#    #sleep(0.1)
#
#    # disable transmission mode
#    #de.off()
#    #re.off()
#
#    print('reading message')
#    rx = s.read(1024)
#    print(rx)


#	while True:
#		# waits for a single character
#		rx = s.read(1024)
#
#		# print the received character
#		print("RX: {0}".format(rx))
#
#		# wait some time before echoing
#		sleep(0.1)
#
#		# enable transmission mode
#		de.on()
#		re.on()
#
#		# echo the received character
#		s.write()
#		s.flush()
#
#		# disable transmission mode
#		#de.off()
#		#re.off()
