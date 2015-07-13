#!/usr/bin/env python

#server...


import time
import getpass
import signal
import select

from serverConnect import NetworkConnect
from button import Button
from lights import Lights
from open_ocd import OpenOCD
from tel_con import TelCon
#from my_file import MyClass

with Lights() as light:
    with NetworkConnect() as network:
        if network.connection() == True:
            while True:
                button.butpush()
                        
                
                with OpenOCD() as openOCD:
                    with TelCon() as telcon:
                                
                        telcon.halt()
                        telcon.erase()
                        telcon.load()
                        light.success()
                network.send("start")
                if "done" in network.receive():
                    light.success()
                User = input("Press <enter> to exit or <spacebar> then <enter> to continue")
                if (User == ""):
                    break

