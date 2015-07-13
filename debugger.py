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
from TogglePower import Reset
#from my_file import MyClass

with Lights() as light:
    with Reset() as powertoggle:
        with NetworkConnect() as network:
            if network.connection() == True:
                while True:
                    with Button() as button:
                        button.butpush()
                                
                        
                        with OpenOCD() as openOCD:
                            with TelCon() as telcon:
                                        
                                telcon.halt()
                                telcon.erase()
                                telcon.load()
                                light.success()
                        powertoggle.toggle()
                        try:
                            network.send("start")
                            if "done" in network.receive():
                                light.success()
                        except:
                            light.failed()
                            sys.exit()
                        User = input("Press <enter> to exit or <spacebar> then <enter> to continue")
                        if (User == ""):
                            break

