#!/usr/bin/env python

import logging
from clientConnect import NetworkConnect
from button import Button
from lights import Lights
from open_ocd import OpenOCD
from tel_con import TelCon
from TogglePower import Reset
from timeout import Timeout
import time

if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    while True:
        try:
            toggle = Reset()
            toggle.toggleOff()
            with Lights(logger.getChild('lights')) as light:  
                with Button(logger.getChild('button')) as button:
                    button.wait_for_button_press()
                    toggle.toggleOn()
                    time.sleep(0.1)
                    light.busy()
                    with Timeout(seconds=20) as t:
                        try:
                            with OpenOCD(logger.getChild('openocd')) as openOCD:
                                with TelCon(logger.getChild('telcon')) as telcon:   
                                    telcon.halt()
                                    telcon.remove_protection()
                                    telcon.halt()
                                    telcon.erase()
                                    telcon.load()
                                    #light.success()
                        except:
                            logging.warn("Provisioning failed")
                            light.busyOff()
                            light.failed()
                            continue
                        toggle.toggle()
                        try:
                            with NetworkConnect(logger.getChild('network')) as connection:
                                connection.send("start")
                                if "done" in connection.receive():
                                    logging.debug("Firmware updated successfully")
                                    light.busyOff()
                                    light.success()
                                else:
                                    logging.debug("Firmware update failed")
                                    light.busyOff()
                                    light.failed()
                                    continue
                        except:
                            light.busyOff()
                            light.failed()
                            logging.critical("Error in netowrk connection")
        except Exception:
            logging.critical("Lights or button initialisation failed")
