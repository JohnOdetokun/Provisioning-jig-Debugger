
import os
import sys
import pexpect
import time
import logging

class UpgradeFailed(Exception):
    pass

class UpgradeSTLink:
    def __init__(self):
        logging.basicConfig()
        self.upgrade = pexpect.spawn("java -jar ./STLinkUpgrade.jar -jtag", timeout=8)
        time.sleep(2)
        upgrade_result = self.upgrade.expect([
            "[\s\S]*Upgrade is successful.",
            "Detected firmware is up to date[\s\S]*",
            "ST-Link is not in the DFU mode.",
            "No ST-Link detected"])
        if upgrade_result == 0:
            logging.info("Firmware upgeaded")
        elif upgrade_result == 1:
            logging.info("upgraded or already the latest version")
        else:
            logging.critical("something went wrong")
            raise UpgradeFailed()
           
