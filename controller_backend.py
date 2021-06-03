'''
    This file is part of RP100 Controller.

    RP100 Controller is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RP100 Controller is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with RP100 Controller.  If not, see <https://www.gnu.org/licenses/>.
'''

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
        # if re.search('^ttyS', deviceString):
        #     possibleDevices.append(deviceString)
        if re.search('^ttyUSB', deviceString):
            possibleDevices.append(deviceString)
        if re.search('^ttyACM', deviceString):
            possibleDevices.append(deviceString)
    possibleDevices = tuple(possibleDevices)
    return possibleDevices

# print(listPossibleSerials())


class rp100:
    serialConnection = None
    deviceID = None
    def writeBytes(self,bytesToBeWritten):
        # get rid of anything incoming from the device before writing
        # self.serialConnection.reset_input_buffer()
        print(bytesToBeWritten)
        self.serialConnection.write(bytesToBeWritten)
    def readBytes(self,numToRead = 100):
        self._readBytes = self.serialConnection.read(numToRead)
        print(self._readBytes)
        return self._readBytes
    def resetDevice(self):
        self.writeBytes(b'*RST\r\n')
    def clearErrs(self):
        self.writeBytes(b'*CLS\r\n')
    def getSetVoltage(self,deviceNum=1):
        _writeBytes = b'SOUR'+bytes(str(deviceNum),'utf-8')+b':VOLT?\r\n'
        self.writeBytes(_writeBytes)
        self._sVolt = self.readBytes()
        return float(self._sVolt)
    def getCurSetVoltage(self,deviceNum=1):
        _writeBytes = b'SOUR'+bytes(str(deviceNum),'utf-8')+b':VOLT:NOW?\r\n'
        self.writeBytes(_writeBytes)
        self._sVolt = self.serialConnection.read(100)
        return float(self._sVolt)
    def measVoltage(self,deviceNum=1):
        _writeBytes = b'MEAS'+bytes(str(deviceNum),'utf-8')+b':VOLT?\r\n'
        self.writeBytes(_writeBytes)
        self._mVolt = self.readBytes()
        return float(self._mVolt)
    def getSetSlew(self,deviceNum=1):
        _writeBytes = b'SOUR'+bytes(str(deviceNum),'utf-8')+b':VOLT:SLEW?\r\n'
        self.writeBytes(_writeBytes)
        self._sSlew = self.readBytes()
        return float(self._sSlew)
    def setVoltage(self,deviceNum=1,numVolts = 0.0):
        _writeBytes = b'SOUR'+bytes(str(deviceNum),'utf-8')+b':VOLT ' + bytes(str(numVolts),'utf-8') + b'\r\n'
        self.writeBytes(_writeBytes)
    def setSlew(self,deviceNum=1,numSlew = 0.0):
        _writeBytes = b'SOUR'+bytes(str(deviceNum),'utf-8')+b':VOLT:SLEW ' + bytes(str(numSlew),'utf-8') + b'\r\n'
        self.writeBytes(_writeBytes)
    def enableDevice(self,deviceNum=1):
        _writeBytes = b'OUTP'+bytes(str(deviceNum),'utf-8') + b' 1\r\n'
        self.writeBytes(_writeBytes)
    def disableDevice(self,deviceNum=1):
        _writeBytes = b'OUTP'+bytes(str(deviceNum),'utf-8') + b' 0\r\n'
        self.writeBytes(_writeBytes)
        
    def __init__(self, serialPort, prependDev=True):
        openUSBPort = serialPort
        if prependDev is True:
            openUSBPort = '/dev/' + openUSBPort
        self.serialConnection = srl.Serial(openUSBPort,timeout=0.05)
        # clear any errors, reset device to just turned on.
        self.clearErrs()
        self.resetDevice()
        self.writeBytes(b'*IDN?\r\n')
        self.deviceID = self.readBytes().decode('utf-8')




