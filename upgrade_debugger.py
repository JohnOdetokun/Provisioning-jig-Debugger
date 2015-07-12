
import os
import sys
import pexpect
import time

class UpgradeSTLink:

    def __init__(self):
        
        self.upgrade = pexpect.spawn("java -jar ~/Desktop/Provisioning-jig-Debugger/st-linkv2_upgrade/AllPlatforms/STLinkUpgrade.jar -jtag", timeout=4)
        time.sleep(2)
        upgrade_state = self.upgrade.expect(["[\s\S]*Upgrade is successful.","Detected firmware is up to date[\s\S]*","No ST-Link detected"])
        
        if upgrade_state == 0 or update_state == 1:
            print("upgraded or already the latest version")
            
        else:
            print("something went wrong")
           

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("BYE!!")
        sys.exit()
        

            
