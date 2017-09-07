from tkinter import *

global myTextVar

root = Tk()

MainFrame = Frame(root, bg="blue")
StatFrame = Frame(root, width=400, height=250, bg="red")
InfoFrame = Frame(root, width=400, height=250, bg="green")



MainFrame.grid(rowspan=2, column=0)
StatFrame.grid(row=0, column=1)
InfoFrame.grid(row=1,column=1)

def clickButton(button,row,col):
    #do something
    if button['text'] == "##":
        myInfo = button.grid_info(); #myRow = ; myCol = myInfo['column']
        button.config(text = myArray[myInfo['row']][myInfo['column']])
    else:
        button.config(text="##")

myArray = [("#","#","#","#","#","#","#","#","#","#")
            ,(10,11,12,13,14,15,16,17,18,19)
            ,(20,21,22,23,24,25,26,27,28,29)
            ,(30,31,32,33,34,35,36,37,38,39)
            ,(40,41,42,43,44,45,46,47,48,49)
            ,(50,51,52,53,54,55,56,57,58,59)
            ,(60,61,62,63,64,65,66,67,68,69)
            ,(70,71,72,73,74,75,76,77,78,79)
            ,(80,81,82,83,84,85,86,87,88,89)
            ,(90,91,92,93,94,95,96,97,98,99)]

for each in myArray:
    for item in each:
        myRow = myArray.index(each); myCol = each.index(item)
        #print(myRow,":",myCol,":",item)
        b=Label(MainFrame,text=item, width=3, borderwidth=1, relief="ridge")
        #b.config(command=lambda b=b: clickButton(b,myRow,myCol))
        b.grid(row=myRow, column=myCol)

mainloop()
