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

with Lights() as light:
    
    with NetworkConnect() as network:
        ("Attempting to connect")
        while network.connection() == True:
            
        
            with Button() as button:
            
                button.butpush()
                with OpenOCD() as openOCD:
                    with TelCon() as telcon:
                                
                        telcon.halt()
                        telcon.erase()
                        telcon.load()
                        light.success()
            with Reset() as powertoggle:
                powertoggle.toggle()
            
            try:
                network.send("start")
                time.sleep(3)
                if "done" in network.receive():
                    light.success()
                else:
                    light.failed()
                    flag = False
            except:
                light.failed()
                flag = False
                sys.exit()
                        

