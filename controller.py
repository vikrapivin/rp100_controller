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

import tkinter as tk
import serial as srl
import controller_backend as ctbe

mainWindow = tk.Tk()
mainWindow.title('RP100 Controller')

#small tk functions
def set_text(entryThing, text):
    entryThing.delete(0,tk.END)
    entryThing.insert(0,text)
    return

frame = tk.Frame(
    master=mainWindow,
    relief=tk.RAISED,
    borderwidth=2
)
frame.grid(row=0, column=0)
mainWindow.grid_rowconfigure(0, weight=1)
mainWindow.grid_columnconfigure(0, weight=1)

curDevice = None
device1Enabled = False
device2Enabled = False
msUpdateSpeed = 1000
# graphics methods
def updateVolts():
    # curVolt1= curDevice.getSetVoltage()
    curVolt1= curDevice.measVoltage()
    print(curVolt1)
    set_text(source1CurVoltage,str(curVolt1))
    # curVolt2= curDevice.getSetVoltage(deviceNum=2)
    curVolt2= curDevice.measVoltage(deviceNum=2)
    print(curVolt2)
    set_text(source2CurVoltage,str(curVolt2))
    mainWindow.after(msUpdateSpeed, updateVolts)
def updateSlew():
    curSlew1= curDevice.getSetSlew()
    set_text(source1CurSlew,str(curSlew1))
    curSlew2= curDevice.getSetSlew(deviceNum=2)
    set_text(source2CurSlew,str(curSlew2))
    mainWindow.after(msUpdateSpeed, updateSlew)
def openNewDevice(*args):
    print(chosenDevice.get())
    print('opening new device above.')
    curDevice = ctbe.rp100(chosenDevice.get())
def toggleDevice1():
    global device1Enabled
    if device1Enabled == False:
        curDevice.enableDevice()
        device1Enabled = True
    else:
        curDevice.disableDevice()
        device1Enabled = False
def toggleDevice2():
    global device2Enabled
    if device2Enabled == False:
        curDevice.enableDevice(deviceNum=2)
        device2Enabled = True
    else:
        curDevice.disableDevice(deviceNum=2)
        device2Enabled = False
def addFiveVoltsDevice1():
    curSetVolt = curDevice.getSetVoltage()
    curDevice.setVoltage(numVolts=curSetVolt + 5.0)
def subtractFiveVoltsDevice1():
    curSetVolt = curDevice.getSetVoltage()
    curDevice.setVoltage(numVolts = curSetVolt - 5.0)
def addFiveVoltsDevice2():
    curSetVolt = curDevice.getSetVoltage(deviceNum=2)
    curDevice.setVoltage(deviceNum=2,numVolts = curSetVolt + 5.0)
def subtractFiveVoltsDevice2():
    curSetVolt = curDevice.getSetVoltage(deviceNum=2)
    curDevice.setVoltage(deviceNum=2,numVolts = curSetVolt - 5.0)
def multiplySlewBy10Device1():
    curSetSlew = curDevice.getSetSlew()
    curDevice.setSlew(numSlew=curSetSlew * 10.0)
def divideSlewBy10Device1():
    curSetSlew = curDevice.getSetSlew()
    curDevice.setSlew(numSlew = curSetSlew / 10.0)
def multiplySlewBy10Device2():
    curSetSlew = curDevice.getSetSlew(deviceNum=2)
    curDevice.setSlew(deviceNum=2,numSlew = curSetSlew* 10.0)
def divideSlewBy10Device2():
    curSetSlew = curDevice.getSetSlew(deviceNum=2)
    curDevice.setSlew(deviceNum=2,numSlew = curSetSlew / 10.0)
def zeroStrainCell():
    # get current set parameters, but I do not think this is necessary to do
    # originalSlewRate1 = curDevice.getSetSlew(deviceNum=1)
    # originalSlewRate2 = curDevice.getSetSlew(deviceNum=2)
    # curSetVolt1 = curDevice.getSetVoltage(deviceNum=1)
    # curSetVolt2 = curDevice.getSetVoltage(deviceNum=2) # 
    curDevice.setSlew(deviceNum=1,numSlew = 100.0)
    curDevice.setSlew(deviceNum=2,numSlew = 100.0)
    curDevice.setVoltage(deviceNum=1,numVolts = 100.0)
    curDevice.setVoltage(deviceNum=2,numVolts = 100.0)
    # wait two minutes and then have it go back
    mainWindow.after(1000*120, zeroStrainCellPart2)
    zeroStrainButton["state"] = tk.DISABLED
    zeroStrainButton["text"] = "Zeroing-In Process"
    return
def zeroStrainCellPart2():
    curDevice.setSlew(deviceNum=1,numSlew = 1.0)
    curDevice.setSlew(deviceNum=2,numSlew = 1.0)
    curDevice.setVoltage(deviceNum=1,numVolts = 0.0)
    curDevice.setVoltage(deviceNum=2,numVolts = 0.0)
    zeroStrainButton["state"] = tk.NORMAL
    zeroStrainButton["text"] = "Zero the Strain Cell"
    return

# source 1
source1Label = tk.Label(master=frame, text='Source 1')
source1Label.grid(row=0, column=0, columnspan=3)
source1StatusChangeButton = tk.Button(
    master=frame, 
    text="Enable/Disable Source 1",
    width=25,
    height=3,
    bg="white",
    fg="black",
    command = toggleDevice1,
)
source1StatusChangeButton.grid(row=1, column=0, columnspan=3)
# voltage controls
source1LessVoltage = tk.Button(
    master=frame, 
    text="Minus 5 Volts",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = subtractFiveVoltsDevice1,
)
source1LessVoltage.grid(row=2, column=0)
source1CurVoltage = tk.Entry(
    master=frame, 
    text='0.0',
    justify=tk.CENTER,
    width=7,
)
source1CurVoltage.grid(row=2, column=1)
source1MoreVoltage = tk.Button(
    master=frame, 
    text="Plus 5 Volts",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = addFiveVoltsDevice1,
)
source1MoreVoltage.grid(row=2, column=2)
# source 1 voltage slew controls
source1LessSlew = tk.Button(
    master=frame, 
    text="Divide Slew by 10",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = divideSlewBy10Device1,
)
source1LessSlew.grid(row=3, column=0)
source1CurSlew = tk.Entry(
    master=frame,
    justify=tk.CENTER,
    width=7,
)
source1CurSlew.grid(row=3, column=1)
source1MoreSlew = tk.Button(
    master=frame, 
    text="Multiply Slew by 10",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = multiplySlewBy10Device1,
)
source1MoreSlew.grid(row=3, column=2)

# source 2
source2Label = tk.Label(master=frame, text='Source 2')
source2Label.grid(row=0, column=3, columnspan=3)
source2StatusChangeButton = tk.Button(
    master=frame, 
    text="Enable/Disable Source 2",
    width=25,
    height=3,
    bg="white",
    fg="black",
    command = toggleDevice2,
)
source2StatusChangeButton.grid(row=1, column=3, columnspan=3)
source2LessVoltage = tk.Button(
    master=frame, 
    text="Minus 5 Volts",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = subtractFiveVoltsDevice2,
)
source2LessVoltage.grid(row=2, column=3)
source2CurVoltage = tk.Entry(
    master=frame,
    justify=tk.CENTER,
    width=7,
)
source2CurVoltage.grid(row=2, column=4)
source2MoreVoltage = tk.Button(
    master=frame, 
    text="Plus 5 Volts",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = addFiveVoltsDevice2,
)
source2MoreVoltage.grid(row=2, column=5)
# source 2 voltage slew controls
source2LessSlew = tk.Button(
    master=frame, 
    text="Divide by 10",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = divideSlewBy10Device2,
)
source2LessSlew.grid(row=3, column=3)
source2CurSlew = tk.Entry(
    master=frame,
    justify=tk.CENTER,
    width=7,
)
source2CurSlew.grid(row=3, column=4)
source2MoreSlew = tk.Button(
    master=frame, 
    text="Multiply by 10",
    width=8,
    height=3,
    bg="white",
    fg="black",
    command = multiplySlewBy10Device2,
)
source2MoreSlew.grid(row=3, column=5)



comDevices = tuple(ctbe.listPossibleSerials())
chosenDevice = tk.StringVar()
chosenDevice.set(comDevices[-1])
curDevice = ctbe.rp100(chosenDevice.get())
deviceDropdown = tk.OptionMenu(frame, chosenDevice, *comDevices, command = openNewDevice)
deviceDropdown.grid(row=4,column =2,columnspan=3)

zeroStrainButton = tk.Button(
    master=frame, 
    text="Zero the Strain Cell",
    width=15,
    height=3,
    bg="white",
    fg="black",
    command = zeroStrainCell,
)
zeroStrainButton.grid(row=4, column=0,columnspan=2)

mainWindow.after(msUpdateSpeed, updateVolts)
mainWindow.after(msUpdateSpeed, updateSlew)
#start window
mainWindow.mainloop()
