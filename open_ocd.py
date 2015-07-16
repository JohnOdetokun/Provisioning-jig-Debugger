import pexpect
import time
import os
import logging
from lights import Lights
class OpenOCDFailed(Exception):
    pass

class OpenOCD:
    
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f1x_stlink.cfg", timeout=3)
        openocd_start_state = self.ocd.expect([
                "Open On-Chip Debugger[\s\S]*hardware has 6 breakpoints, 4 watchpoints",
                "Error: open failed",
                "Error: couldn't bind to socket: Address already in use"
                "init mode failed \(unable to connect to the target\)"
        ])
        if openocd_start_state == 0:
            logging.info("On-Chip debugger opened")            
        elif openocd_start_state == 1:
            logging.critical("openOCD failed")
            raise OpenOCDFailed()
        elif openocd_start_state == 2:
            os.system("killall openocd")
            logging.critical("openocd already active.... Now closed, run program again")
            raise OpenOCDFailed()
        else:
            logging.critical("Unexpected problem")
            raise OpenOCDFailed()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.ocd.terminate()
        logging.info("OpenOCD terminated")
