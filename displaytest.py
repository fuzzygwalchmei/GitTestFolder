from tkinter import *

global myTextVar

root = Tk()

myFrame = Frame(root, width=500, height=500)

myFrame.pack()

def btnClicked(myButton):
    myValue = myButton.grid_info()
    myRow=myValue['row']
    myCol=myValue['column']
    myCoord = myRow
    myLabelOne.config(text=myCoord)


for i in range(5):
    b = Button(myFrame, text="Button "+str(i))
    b.config(command =lambda b=b:btnClicked(b))
    b.grid(row=i+1, column=0)




myLabelOne = Label(myFrame, text="My Label")
myLabelOne.grid(row=0, columnspan=2)

mainloop()
