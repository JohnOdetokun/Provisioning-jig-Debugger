
import os
import sys
import pexpect
import time

class UpgradeSTLink:

    def __init__(self):
        
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
        else:
            print("something went wrong")
           

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("BYE!!")
        sys.exit()
        

            
