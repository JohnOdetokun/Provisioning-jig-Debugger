#!/usr/bin/env python

import logging
from clientConnect import NetworkConnect
from button import Button
from lights import Lights
from open_ocd import OpenOCD
from tel_con import TelCon
from TogglePower import Reset
from timeout import Timeout

if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    while True:
        try:
            with Lights(logger.getChild('lights')) as light:  
                with Button(logger.getChild('button')) as button:
                    button.wait_for_button_press()
                    light.busy()
                    try:
                        with OpenOCD(logger.getChild('openocd')) as openOCD:
                            with TelCon(logger.getChild('telcon')) as telcon:   
                                telcon.halt()
                                telcon.remove_protection()
                                telcon.halt()
                                telcon.erase()
                                telcon.load()
                                light.success()
                    except:
                        logging.warn("Provisioning failed")
                        light.failed()
                        continue
                toggle = Reset()
                toggle.toggle()
                try:
                    with NetworkConnect(logger.getChild('network')) as connection:
##                        with timeout(seconds=10):
                        connection.send("start")
                        if "done" in connection.receive():
                            logging.debug("Firmware updated successfully")
                            light.success()
                        else:
                            logging.debug("Firmware update failed")
                            light.failed()
                            continue
                except:
                    light.failed()
                    logging.critical("Error in netowrk connection")
        except Exception:
            logging.critical("Lights or button initialisation failed")
