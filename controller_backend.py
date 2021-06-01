import serial as srl
import subprocess
import re


# return possible tty's to open
def listPossibleSerials():
    findPossibleConnections = subprocess.run(
        ['ls', '/dev/'],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )
    possibleDevices = []
    for deviceString in findPossibleConnections.stdout.splitlines():
        if re.search('^ttyS', deviceString):
            possibleDevices.append(deviceString)
        if re.search('^ttyUSB', deviceString):
            possibleDevices.append(deviceString)
    possibleDevices = tuple(possibleDevices)
    return possibleDevices

# print(listPossibleSerials())







