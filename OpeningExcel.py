import mysql.connector
import csv
from tkinter import *

def callback():
    commentWindow.config(text=entryWindow.get())

def update_database():
    database = mysql.connector.connect (database = "demodb", user="root", password="MySQLPassword", host="localhost", port="3306")
    cursor = database.cursor()
    #mydata = cursor.execute(delete)
    with open('Sup_Data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #for row in spamreader:
        #    print(row)
        #    cursor.execute("""INSERT INTO Supplier_List VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", row)
    CLearDB = "Delete from Supplier_List"
    cursor.execute(CLearDB)
    fileVariable = entryWindow.get()
    query = "LOAD DATA LOCAL INFILE '"+fileVariable+"' INTO TABLE Supplier_List FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 0 LINES;"
    cursor.execute(query)
    cursor.close()
    database.commit()
    database.close()

    commentWindow.config(text = "Database updated")

def compareFile():
    compareFileName = compareWindow.get()
    database = mysql.connector.connect (database = "demodb", user="root", password="MySQLPassword", host="localhost", port="3306")
    cursor = database.cursor()
    with open(compareFileName, 'r') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for each in spamreader:
            try:
                checkValue = each["supplier_name"]
                print(checkValue)
                sqlQuery="""SELECT * FROM Supplier_List WHERE supplier_name = '%s' and is_verified = 't'""" % (checkValue)
                cursor.execute(sqlQuery)
                myData = cursor.fetchall()
                print(myData)
            except:
                print("Column not available")
                break

    database.close()


#Start Main
rootWindow = Tk()
rootWindow.title("Supplier Checker")
rootWindow.geometry('300x75+800+200')

#Define main window
inputWindow = Frame(rootWindow, width=150, height=75, bg="red")
inputWindow.grid(row=0, column=0, sticky='nsew');rootWindow.rowconfigure(0,weight=1);rootWindow.columnconfigure(0,weight=1)
buttonWindow = Frame(rootWindow, width=150, height=75, bg="green")
buttonWindow.grid(row=0, column=1, sticky='nsew');rootWindow.rowconfigure(0,weight=1);rootWindow.columnconfigure(1,weight=1)

#Create and structure main window
entryWindow = Entry(inputWindow)
entryWindow.grid(row=0,column=0, sticky="nsew");inputWindow.rowconfigure(0,weight=1);inputWindow.columnconfigure(0,weight=1)
compareWindow = Entry(inputWindow)
compareWindow.grid(row=1, column=0, sticky="nsew");inputWindow.rowconfigure(1,weight=1);inputWindow.columnconfigure(0,weight=1)
commentWindow = Label(inputWindow,text="Starting Text")
commentWindow.grid(row=2,column=0, sticky="nsew");inputWindow.rowconfigure(2,weight=1);inputWindow.columnconfigure(0,weight=1)

#Create and structure Button window
selectFileButton = Button(buttonWindow, text="Select File", command=callback)
selectFileButton.grid(row=0, column=0, sticky="nsew");buttonWindow.rowconfigure(0,weight=1);buttonWindow.columnconfigure(0,weight=1)
compareButton = Button(buttonWindow, text="Compare File", command=compareFile)
compareButton.grid(row=1, column=0, sticky="nsew");buttonWindow.rowconfigure(1,weight=1);buttonWindow.columnconfigure(0,weight=1)
updateFileButton = Button(buttonWindow, text="Update File", command=update_database)
updateFileButton.grid(row=2, column=0, sticky="nsew");buttonWindow.rowconfigure(2,weight=1);buttonWindow.columnconfigure(0,weight=1)

#run the mainloop()
mainloop()
