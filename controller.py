import tkinter as tk
import serial as srl
import controller_backend as ctbe

mainWindow = tk.Tk()
mainWindow.title('RP100 Controller')

frame = tk.Frame(
    master=mainWindow,
    relief=tk.RAISED,
    borderwidth=2
)
frame.grid(row=0, column=0)
mainWindow.grid_rowconfigure(0, weight=1)
mainWindow.grid_columnconfigure(0, weight=1)
source1Label = tk.Label(master=frame, text='Source 1')
source1Label.grid(row=0, column=0, columnspan=3)
source1StatusChangeButton = tk.Button(
    master=frame, 
    text="Enable/Disable Source 1",
    width=25,
    height=5,
    bg="white",
    fg="black",
)
source1StatusChangeButton.grid(row=1, column=0, columnspan=3)
# voltage controls
source1LessVoltage = tk.Button(
    master=frame, 
    text="Minus 5 Volts",
    width=8,
    height=5,
    bg="white",
    fg="black",
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
    height=5,
    bg="white",
    fg="black",
)
source1MoreVoltage.grid(row=2, column=2)
# source 1 voltage slew controls
source1LessSlew = tk.Button(
    master=frame, 
    text="Minus 1 V/s",
    width=8,
    height=5,
    bg="white",
    fg="black",
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
    text="Plus 1 V/s",
    width=8,
    height=5,
    bg="white",
    fg="black",
)
source1MoreSlew.grid(row=3, column=2)

# source 2
source2Label = tk.Label(master=frame, text='Source 2')
source2Label.grid(row=0, column=3, columnspan=3)
source2StatusChangeButton = tk.Button(
    master=frame, 
    text="Enable/Disable Source 2",
    width=25,
    height=5,
    bg="white",
    fg="black",
)
source2StatusChangeButton.grid(row=1, column=3, columnspan=3)
source2LessVoltage = tk.Button(
    master=frame, 
    text="Minus 5 Volts",
    width=8,
    height=5,
    bg="white",
    fg="black",
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
    height=5,
    bg="white",
    fg="black",
)
source2MoreVoltage.grid(row=2, column=5)
# source 2 voltage slew controls
source2LessSlew = tk.Button(
    master=frame, 
    text="Minus 1 V/s",
    width=8,
    height=5,
    bg="white",
    fg="black",
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
    text="Plus 1 V/s",
    width=8,
    height=5,
    bg="white",
    fg="black",
)
source2MoreSlew.grid(row=3, column=5)
def printCur(*args):
    print(chosenDevice.get())
comDevices = tuple(ctbe.listPossibleSerials())
chosenDevice = tk.StringVar()
chosenDevice.set(comDevices[-1])
deviceDropdown = tk.OptionMenu(frame, chosenDevice, *comDevices, command = printCur)
deviceDropdown.grid(row=4,columnspan=6)
#start window
mainWindow.mainloop()
