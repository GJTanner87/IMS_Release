import tkinter as tk
from PIL import ImageTk, Image
import serial.tools.list_ports
import serial
import time
import csv
#import imagetest
#import porttest
#import socket
import telnetlib

ports = serial.tools.list_ports.comports()
portList = []
#window = tk.Tk()

#canvas1 = tk.Canvas(root, width = 500, height = 800)

#Lb1 = tk.Listbox(root, width= 500, height=5, selectmode= "SINGLE")



output = " "
#ser = serial.Serial('/dev/ttyUSB0', 4800, 8, 'N', 1, timeout=1)
#ipaddress = '10.200.1.3'
#ipaddress = '10.1.5.0'
TCP_PORT = 10001
portLabel = 'COM1'
portVar = 'Initial'
#ipaddress = '111.111.111.111'
mess_count = 0
port_selected = 0
switch = 1
loop_count = 0
switch1_press = 'Not Pressed'
switch2_press = 'Not Pressed'
#pos_count = 1

#This creates the main window of an application
window = tk.Tk()
window.title("Flann Microwave")
window.geometry("1225x800")
window.configure(background='light grey')

prvaLabel = tk.Label()
valueLabel = tk.Label()

#path = "LOGO STACKED 1172 x 388mm 72dpi 00031812_01_A1.jpg"
path = "NewFlannWithTag.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "top", fill = "both", expand = "yes")
panel.place(x=10, y=5)
canvas1 = tk.Canvas(window, width= 500, height= 800)

dBenter = tk.Text(window, height= 2, width= 40,  font= ('helvetica', 16, 'bold'))
ipEnter = tk.Text(window, height= 2, width= 85)


serialInst = serial.Serial()

posList = []

#tn = telnetlib.Telnet(ipaddress, TCP_PORT)
Lb1 = tk.Listbox(window, width= 85, height=3, selectmode= "SINGLE")
Lb2 = tk.Listbox(window, width=30, height= 10, font= ('helvetica', 12, 'bold'))
#PoB1 = tk.Listbox(window, width = 50, height = 30, selectmode = "multiple")

def get_ports():
    global portList
    portList = []
    for onePort in ports:
        loop = 1
        portList.append(str(onePort))
    
    print(str(onePort))
    loop = loop +1



def pop_ports(Lb1):

    for x in range(0,len(portList)):
        Lb1.insert(x, portList[x])
        print(portList[x])


def load_ports():
    Lb1.delete(0,'end')
    #porttest.get_ports()
    get_ports()
    receiveWindow= canvas1.create_window(250, 600)
    pop_ports(Lb1)
    #porttest.pop_ports(Lb1)

def serial_selection():
    global portLabel
    global portVar
    global output
    global port_selected

    for i in Lb1.curselection():
        print(Lb1.get(i))
        #canvas1.delete("all")
    portTmp = Lb1.get(i)
    portVar = portTmp[:4]
    portLabel = tk.Label(window, background= 'light grey', text= 'Port Selected:' +portVar, fg = 'green', font= ('helvetica', 12, 'bold'))
    portLabel.place(x=850, y=775)
    #canvas1.create_window(150, 120, window=portLabel)
    serialInst.port = portVar
    serialInst.baudrate = 9600
    serialInst.open()
    port_selected = 1
    check_pos()



def switch1Pos1():
    global message
    global switch
    global switch1_press

    message = '337 1 Position 1'
#              012345678901234567
    switch1_press = 'Position 1    '
    switch = 1
    usbMessage = message
    #canvas2.delete("all")
    #commandLabel = tk.Label(root, text=message, fg='red', font= ('helvetica', 12, 'bold'))
    #canvas2.create_window(150, 30, window= commandLabel)
    if message == ('exit' or 'EXIT' or 'Exit'):
        serialInst.close()
        exit()
    else:
        usbMessage = str(usbMessage) + '\n\r'
        serialInst.write(usbMessage.encode('utf'))
        usb_wait()
        check_pos()
        #output()
        out = ''

def switch1Pos2():
    global message
    global switch
    global switch1_press

    message = '337 1 Position 2'
#              012345678901234567
    switch1_press = 'Position 2    '
    switch = 1
    usbMessage = message
    #canvas2.delete("all")
    #commandLabel = tk.Label(root, text=message, fg='red', font= ('helvetica', 12, 'bold'))
    #canvas2.create_window(150, 30, window= commandLabel)
    if message == ('exit' or 'EXIT' or 'Exit'):
        serialInst.close()
        exit()
    else:
        usbMessage = str(usbMessage) + '\n\r'
        serialInst.write(usbMessage.encode('utf'))
        usb_wait()
        check_pos()
        #output()
        out = ''

def switch2Pos1():
    global message
    global switch
    global switch2_press

    message = '337 2 Position 1'
#              012345678901234567
    switch2_press = 'Position 1    '
    switch = 2
    usbMessage = message
    #canvas2.delete("all")
    #commandLabel = tk.Label(root, text=message, fg='red', font= ('helvetica', 12, 'bold'))
    #canvas2.create_window(150, 30, window= commandLabel)
    if message == ('exit' or 'EXIT' or 'Exit'):
        serialInst.close()
        exit()
    else:
        usbMessage = str(usbMessage) + '\n\r'
        serialInst.write(usbMessage.encode('utf'))
        usb_wait()
        check_pos()
        #output()
        out = ''

def switch2Pos2():
    global message
    global switch
    global switch2_press

    message = '337 2 Position 2'
#              012345678901234567
    switch2_press = 'Position 2    '
    switch = 2
    usbMessage = message
    #canvas2.delete("all")
    #commandLabel = tk.Label(root, text=message, fg='red', font= ('helvetica', 12, 'bold'))
    #canvas2.create_window(150, 30, window= commandLabel)
    if message == ('exit' or 'EXIT' or 'Exit'):
        serialInst.close()
        exit()
    else:
        usbMessage = str(usbMessage) + '\n\r'
        serialInst.write(usbMessage.encode('utf'))
        usb_wait()
        check_pos()
        #output()
        out = ''

def output(position):
    global message
    #pos_count = 0
    global mess_count

    posList.append(position)
    mess_count = mess_count + 1
    switch1Label = tk.Label(window, text= 'Last Pressed: ' +str(switch1_press), fg= 'green', background= 'light grey', font=('helvetica', 16,'bold'))
    switch2Label = tk.Label(window, text= 'Last Pressed: ' +str(switch2_press), fg= 'green', background= 'light grey', font=('helvetica', 16,'bold'))
    switch1Label.place(x=625,y=420)
    switch2Label.place(x=925,y=420)
    #pos_count = pos_count + 1
    #with open('pos_data.csv', 'w', newline='') as csvfile:
    #    poswriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #    for pos_count in posList:
    #        poswriter.writerow(pos_count)
    #posList[pos_count] = position
   #PoB1.insert(pos_count, position)
    #print(posList[pos_count])
    #

def clear_labels():
    valueLabel = tk.Label(window, text= ' ', fg = 'green', background='white', font=('helvetica', 12,'bold'))
    valueLabel.place(x=400, y = 600)

def movePRVA():
    global message
    
    clear_labels()
    dbvalue = dBenter.get("1.0", "end-1c")
#    tn = telnetlib.Telnet(ipaddress, TCP_PORT)
    print(dbvalue)
    message = ('VALUE_SET'+ str(dbvalue) + '\r\n')
    tn.write(message.encode('utf-8'))
    print(message)
    prvaLabel = tk.Label(window, text= '625 PVRA Position: ' +str(dbvalue) +' dB   ', fg = 'green', background='light grey', font=('helvetica', 20,'bold'))
    prvaLabel.place(x=110, y = 370)
    message = str('VALUE_SET?\r\n')
    tn.write(message.encode('utf-8'))
    #tn.write(b'VALUE_SET?\r\n')
    output = tn.read_until(b'\n')
    dBenter.delete("1.0","end-1c")
#    tn.close
    

def sendIdn():
    global message

    message = '*IDN?'
    print(message)


def usb_wait():
        global switch
    #loop = 5
    #for x in range (loop):
        time.sleep(1)
        if serialInst.in_waiting:
            packet = serialInst.readline()
            output_packet = packet.decode('utf').rstrip('\n').rstrip('\r')
            encode = output_packet
            if (switch == 1):
                receive1Label = tk.Label(window, text = output_packet, background= 'white', fg= 'green', font= ('helvetica', 12, 'bold'))
                #receive1Label.place(x=55, y=680)
            if (switch == 2):
                receive2Label = tk.Label(window, text = output_packet, background= 'white', fg= 'green', font= ('helvetica', 12, 'bold'))
                #receive2Label.place(x=205, y=680)
            output(output_packet)
            print(output_packet)

def check_pos():
    global message
    global port_selected
    global switch

    if (port_selected == 1):
        message = 'S1 337 Pos Check'
    #              012345678901234567
        switch = 1
        usbMessage = message
        if message == ('exit' or 'EXIT' or 'Exit'):
            serialInst.close()
            exit()
        else:
            usbMessage = str(usbMessage) + '\n\r'
            serialInst.write(usbMessage.encode('utf'))
            usb_wait()
            #output()
            out = ''

        message = 'S2 337 Pos Check'
    #              012345678901234567
        switch = 2
        usbMessage = message
        if message == ('exit' or 'EXIT' or 'Exit'):
            serialInst.close()
            exit()
        else:
            usbMessage = str(usbMessage) + '\n\r'
            serialInst.write(usbMessage.encode('utf'))
            usb_wait()
            #output()
            out = ''

#    with open('Switch Position.csv', 'w', newline='') as csvfile:
#        for x in range (0,len(posList)):
#            fieldnames = ['Post Test', 'Drive Mode']
#            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
#            writer.writeheader()
#            writer.writerow({'Post Test': posList[x], 'Drive Mode':message})
            #for x in range(0,len(posList)):
            #PoB1.insert(posList[pos_count], pos_count)
            #print(posList[pos_count])
def count():
    global mess_count

    mess_count = mess_count + 1
   # countLabel = tk.Label(window, text = mess_count, font=('helvetica',12,'bold'))
   # countLabel.place(x=600, y=600)

def delete1Pos():
    Lb1.delete(0,'end')

def auto_command():
    message = ('ENG_MODE_ON'+'\n\r')
    tn.write(message.encode('utf-8'))
    message = ('EXET 3'+'\n\r')
    tn.write(message.encode('utf-8'))    
    message = ('ENG_MODE_OFF'+'\n\r')
    tn.write(message.encode('utf-8'))

def stop_auto():
    message = ('ENG_MODE_ON'+'\n\r')
    tn.write(message.encode('utf-8'))
    message = ('EXET 1'+'\n\r')
    tn.write(message.encode('utf-8'))
    message = ('ENG_MODE_OFF'+'\n\r')
    tn.write(message.encode('utf-8'))



#canvas1.pack(side="bottom")
    
count()

load_ports()    
s337Label = tk.Label(window, text= '337 Controls', fg = 'green',background='light grey', font=('helvetica',28,'bold'))
s625Label = tk.Label(window, text= '625 Controls', fg = 'green',background='light grey', font=('helvetica',28,'bold'))
portLabel = tk.Label(window, text = 'COM Port', fg = 'green', background = 'light grey', font=('helvetica',12,'bold'))
s337s1Label = tk.Label(window, text= '337 Switch 1', fg = 'green', background = 'light grey', font=('helvetica',20,'bold'))
s337s2Label = tk.Label(window, text= '337 Switch 2', fg = 'green', background = 'light grey', font=('helvetica',20,'bold'))

s337Label.place(x=800, y=200)
s337s1Label.place(x=675, y=280)
s337s2Label.place(x=975, y=280)
s625Label.place(x=175, y=200)
portLabel.place(x=850, y=675)

Lb1.place(x=650, y=700)
Lb2.place(x =110, y = 490)
#PoB1.place(x=0, y=500)

recentdBLabel = tk.Label(window, text='Recently set positions (dB)', fg='green', background='light grey', font=('helvetica', 20, 'bold','underline'))
recentdBLabel.place(x=90, y=425)

portBtn = tk.Button(window, text= 'Select COM Port', command=serial_selection)
s1pos1Btn = tk.Button(window, text= 'Position 1', font = ('helvetica', 12, 'bold'), command=switch1Pos1)
s1pos2Btn = tk.Button(window, text= 'Position 2', font = ('helvetica', 12, 'bold'), command=switch1Pos2)
s2pos1Btn = tk.Button(window, text = 'Position 1', font = ('helvetica', 12, 'bold'), command=switch2Pos1)
s2pos2Btn = tk.Button(window, text= 'Position 2', font = ('helvetica', 12, 'bold'), command= switch2Pos2)
auto625Btn = tk.Button(window, text = 'Auto Test PRVA', font = ('helvetica', 12, 'bold'), command= auto_command)
stop625Btn = tk.Button(window, text= ' Stop PRVA', font = ('helvetica', 12, 'bold'), command = stop_auto)
prvaBtn = tk.Button(window, text= 'Move PRVA', font = ('helvetica', 12, 'bold'), command= movePRVA)
refreshBtn = tk.Button(window, text= 'Refresh Port List', command= load_ports)
deleteBtn = tk.Button(window, text= 'delete', command=delete1Pos)
idnBtn = tk.Button(window, text='*idn', command=sendIdn)

portBtn.place(x=650, y=770)
auto625Btn.place(x=190, y=330)
stop625Btn.place(x=380, y=330)
#refreshBtn.place(x=150, y=585)
s1pos1Btn.place(x=725, y=325)
s1pos2Btn.place(x=725, y=365)
s2pos1Btn.place(x=1025, y=325)
s2pos2Btn.place(x=1025, y=365)
prvaBtn.place(x=5, y=330)
#ipenBtn.place(x=500, y=570)


dBenter.place(x=5, y=270)
#ipEnter.place(x=500, y=500)

#deleteBtn.pack(side='top')

#while 1:
    #if (portVar != 'Initial'):
    #    print("----")
    #    while output != "":
    #        output = serialInst.readline()
    #        print(output)
    #        output = ""
#    time.sleep(1)
#    loop_count = loop_count + 1
#    if (loop_count > 10):
#        check_pos()
#        loop_count = 0
        #count()
#    window.update()

#Start the GUI
window.mainloop()

