
import os
import sys
import pexpect
import time
import logging

class UpgradeFailed(Exception):
    pass

class UpgradeSTLink:
    def __init__(self):
<<<<<<< HEAD
        
        self.upgrade = pexpect.spawn("java -jar ~/Desktop/Provisioning-jig-Debugger/st-linkv2_upgrade/AllPlatforms/STLinkUpgrade.jar -jtag", timeout=3)
        try: 
            upgrade_state = self.upgrade.expect(["[\s\S]*Upgrade is successful.[\s\S]*","Detected firmware is up to date; use -force_prog to enforce reprogramming.","No ST-Link detected", pexpect.EOF, pexpect.TIMEOUT])
        except EOF:
            print("EOF error")

        if upgrade_state == 0:
            print("upgraded")
        elif upgrade_state == 1:
            print("already the latest version")
        elif(upgrade_state == 3):
            print("EOF problem")
=======
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
>>>>>>> 8b0fde5859d297366b8c37f8653759e9080ce7ac
        else:
            logging.critical("something went wrong")
            raise UpgradeFailed()
           
