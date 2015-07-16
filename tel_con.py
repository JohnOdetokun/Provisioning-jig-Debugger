import pexpect
import re
import sys
import telnetlib
import logging

class TelConFailed(Exception):
    pass

class TelCon:
    def __init__(self, logger = logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        telcon_start = self.tel.expect([
            "Connected to localhost",
            "unable to"
            ])
        if telcon_start == 0:
            logging.info("connected to telnet")
        else:
            raise TelConFailed()

    def __enter__(self):
        return self
    
    def halt(self):
        self.tel.sendline("reset halt")
        self.tel.expect("[\s\S]*target halted[\s\S]*")
        logging.info("halted")

    def remove_protection(self):
        self.tel.sendline("flash protect 0 0 last off")
        self.tel.expect("cleared protection for sectors")
        logging.info("erased")
    
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
        logging.info("Telnet connection terminated")
