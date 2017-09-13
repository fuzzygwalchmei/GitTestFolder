import mysql.connector
import csv

database = mysql.connector.connect (database = "demodb", user="root", password="MySQLPassword", host="localhost", port="3306")
cursor = database.cursor()
delete = """Drop table if exists Real.SampleDataTwo"""
print (delete)

mydata = cursor.execute(delete)


with open('Sup_Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #for row in spamreader:
    #    print(row)
    #    cursor.execute("""INSERT INTO Supplier_List VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", row)

query = "LOAD DATA INFILE '/Sup_Data.csv' INTO TABLE Supplier_List FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n';"

cursor.execute(query)

cursor.close()
database.commit()
database.close()

print ("CSV data imported")
