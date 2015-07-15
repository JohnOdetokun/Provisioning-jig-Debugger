import pexpect
import re
import sys
import telnetlib
import logging
from lights import Lights

class TelCon:
    def __init__(self):
        logging.basicConfig()
        self.c= Lights()
        self.tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        telcon_start = self.tel.expect(["[\s\S]*\nConnected to localhost[\s\S]*", "[\s\S]unable to[\s\S]"])
        if telcon_start == 0:
            logging.info("connected to telnet")
        else:
            self.c.failed()
            sys.exit()

    def __enter__(self):
        return self
    
    def halt(self):
        self.tel.sendline("reset halt")
        self.tel.expect("[\s\S]*target halted[\s\S]*")
        logging.info("halted")

    def erase(self):
        self.tel.sendline("flash erase_sector 0 0 0")
        self.tel.expect("[\s\S]*erased sectors[\s\S]*")
        logging.info("erased")

    def load(self):
        self.tel.sendline("flash write_image erase /root/workspace/Provisioning-jig-Debugger/debug/DFU_ST-Link-V2.hex")
        self.tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")

        self.tel.sendline("verify_image /root/workspace/Provisioning-jig-Debugger/debug/DFU_ST-Link-V2.hex")
        self.tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")
        logging.info("LOADED!")

    def __exit__(self, type, value, traceback):
        self.tel.send("exit")
