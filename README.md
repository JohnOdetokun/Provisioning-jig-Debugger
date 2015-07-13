# Provisioning-jig-Debugger
code to load code onto chip to make chip a debugger

In this repository debugger is the main code that will be 
run on the raspberry pi (2nd one)

This program from serverConnect, button, lights, open_ocd, 
tel_con, TogglePower

program run and then waits for a connection from laptop 
before carrying on.

open_ocd handles openocd connection to debugger.

tel_con handles telnet connection in order to connect 
and load code to target chip(stm32fo)

TogglePower is used to toggle the power to the debug jig

lights is used to disaply success, failure or that the 
program is busy

button is used to determine from a button when to begin 
the loading on to the chip(after connection to laptop is
 established)

