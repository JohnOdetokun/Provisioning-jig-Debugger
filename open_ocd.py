import pexpect
import time
import os
import sys
import logging
from lights import Lights
class OpenOCD:
    
    def __init__(self):
        logging.basicConfig()
        self.c = Lights()
        try:
            
            self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f1x_stlink.cfg", timeout=3)
            openocd_start_state = self.ocd.expect(["Open On-Chip Debugger[\s\S]*hardware has 6 breakpoints, 4 watchpoints[\s\S]*","[\s\S]*Error: open failed[\s\S]*","[\s\S]*Error: couldn't bind to socket: Address already in use[\s\S]*"])
            print(openocd_start_state)
            if openocd_start_state == 0:
                logging.info("On-Chip debugger opened")
                
            elif openocd_start_state == 1:
                logging.critical("openOCD failed")
                c.failed()
                sys.exit()
            elif openocd_start_state == 2:
                os.system("killall openocd")
                logging.critical("openocd already active.... Now closed, run program again")
                c.failed()
                sys.exit()
            
        except:
            print("dunno")
            self.c.failed()
            sys.exit()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("Open OCDs exit command")
        os.system("killall openocd")
