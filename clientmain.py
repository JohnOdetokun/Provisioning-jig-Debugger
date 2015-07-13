from clientConnect import NetworkConnect

with NetworkConnect() as network:
    print(network.receive())
    message = input("Now what do you have to say?")
    network.send(message)
