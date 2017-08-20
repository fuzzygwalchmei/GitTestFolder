from easygui import *
import random
import os
import tkinter

def game_new():
    n = enterbox(msg='Enter your name.', title='Welcome new user!', strip=True)
    while n.strip() == "":
        n = enterbox(msg='Oops you forgot to enter a name!', title='Welcome new user!', strip=True)
    a = buttonbox(msg='Choose a game difficulty', title='Configuration', choices = ['Beginner','Intermediate','Expert','Custom'])
    if a[0] == 'B':
        return n, 9, 9, 10
    elif a[0] == 'I':
        return n, 16, 16, 40
    elif a[0] == 'E':
        return n, 30, 16, 99
    else:
        a,b,c = customconfigure()
        return n,a,b,c

def customconfigure():
    msg = "Minesweeper configuration:"
    title = "Settings"
    fieldNames = ["Width in mines (max 30):","Height in mines (max 20):","Mines:"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" was left blank.\n\n' % fieldNames[i])
            elif not fieldValues[i].strip().isdigit:
                errmsg += ('"%s" must be an integer.\n\n' % fieldNames[i])
            elif i == 0 and not 3 <= int(fieldValues[i]) <= 30:
                errmsg += ('Width must be between 3 and 30 mines.\n\n')
            elif i == 1 and not 3 <= int(fieldValues[i]) <= 20:
                errmsg += ('Height must be between 3 and 20 mines.\n\n')
            elif i == 2 and not 1 <= int(fieldValues[i]) <= (int(fieldValues[0]) * int(fieldValues[1]) - 1):
                errmsg += ('Mines must be between 1 and ' + str(int(fieldValues[0]) * int(fieldValues[1]) - 1) + '\n\n')
        if errmsg == "":
            break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    return int(fieldValues[0]),int(fieldValues[1]),int(fieldValues[2])

def inchk(s,m):
    if not s.isdigit:
        return False
    if 1 <= int(s) <= m:
        return True
    else:
        return False

def move_get():
    user_x = raw_input("Enter the 'x' of the point you want to preform an action on: ")
    while not inchk(user_x,width):
        user_x = raw_input("Invalid selection. Enter a value for 'x': ")
    user_y = raw_input("Enter the 'y' of the point you want to preform an action on: ")
    while not inchk(user_y,height):
        user_y = raw_input("Invalid selection. Enter a value for 'y': ")
    return int(user_x), int(user_y)


def location_reveal(x,y):
    global field
    global showing
    global symbol_mine
    if field[x][y] == symbol_mine:
        game_over()
    else:
        showing[x][y] = " " + str(field[x][y]) + " "
        if showing[x-1][y] == "     " and field[x-1][y] != symbol_mine:
            location_reveal(x-1,y)
        if showing[x+1][y] == "     " and field[x+1][y] != symbol_mine:
            location_reveal(x+1,y)
        if showing[x][y+1] == "     " and field[x][y+1] != symbol_mine:
            location_reveal(x,y+1)
        if showing[x][y-1] == "     " and field[x][y-1] != symbol_mine:
            location_reveal(x,y-1)
    playing()

def location_chosen(s,button):
    global field
    global showing
    x = int(s[:s.index(":")]) + 1
    y = int(s[s.index(":")+1:]) + 1
    msg = "Choose an action to "
    choices = ["Reveal","Flag","Back"]
    reply = buttonbox(msg,choices=choices)
    field_hid.destroy
    if reply == "Back":
        playing()
    elif reply == "Flag":
        showing[x][y] = " F "
        playing()
    else:
        location_reveal(x,y)

def playing():
    global field
    global showing
    global width
    global height
    global symbol_mine
    win = False
    def k():
        field_hid.destroy()
    count_mine = 0
    count_flag = 0
    for x in field:
        count_mine += x.count(symbol_mine)
    for x in showing:
        count_flag += x.count(' F ')
    for x in range(1, width):
        for y in range(1, height):
            if field[x][y] == symbol_mine and showing[x][y] == ' F ':
                if count_mine == count_flag:
                    win = True
                else:
                    win = False
                    break


    field_hid = tkinter.Tk()
    for x in range(width):
        for y in range(height):
            s = str(x) + ":" + str(y)
            t = showing[x+1][y+1]
            b = tkinter.Button(field_hid, text = t)
            b.configure(command = lambda s=s, button=b: location_chosen(s,button))
            #b.bind('<Button-1>', field_hid.destroy())
            #b.pack()
            b.grid(row=x, column=y)
    tkinter.mainloop()

def main():
    global width
    global height
    global field
    global showing
    global symbol_mine
    user_name, width, height, mines = game_new()
    symbol_empty = ' '
    symbol_mine = 'M'
    play = True

    #Creates field with empty spaces
    field = [[symbol_empty for h in range(width+2)] for w in range(height+2)]    #
    showing = [["     " for h in range(width+2)] for w in range(height+2)]

    # Randomly places mines on the field
    mines_placed = 0
    while mines_placed < mines:
        y = random.randint(1,width)#
        x = random.randint(1,height)#
        if field[x][y] == symbol_empty:
            field[x][y] = symbol_mine
            mines_placed += 1

    # Checks How many mines border each square
    for x in range(1,height+1):
        for y in range(1, width+1):
            if field[x][y] != symbol_mine:
                mines_touching = 0
                for x2 in range(x-1,x+2):
                    for y2 in range(y-1,y+2):
                        if field[x2][y2] == symbol_mine:
                            mines_touching += 1
                if mines_touching > 0:
                    field[x][y] = str(mines_touching)

    #Creates the playing field
    playing()

main()
