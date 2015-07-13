from clientConnect import NetworkConnect

with NetworkConnect() as network:
    piCommand = network.receive()
    if "start" in piCommand:
        print("Upgraded")
        network.send("done")
    else:
        network.send("Couldnt upgrade")
