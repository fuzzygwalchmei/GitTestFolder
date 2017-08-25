from tkinter import *

root = Tk()

def clickButton(button,row,col):
    #do something
    if button['text'] == "#":
        myInfo = button.grid_info(); #myRow = ; myCol = myInfo['column']
        button.config(text = myArray[myInfo['row']][myInfo['column']])
    else:
        button.config(text="#")

myArray = [(1,2,3),(4,5,6),(7,8,9)]

for each in myArray:
    for item in each:
        myRow = myArray.index(each); myCol = each.index(item)
        print(myRow,":",myCol,":",item)
        b=Button(root,text=item)
        b.config(command=lambda b=b: clickButton(b,myRow,myCol))
        b.grid(row=myRow, column=myCol)



mainloop()
