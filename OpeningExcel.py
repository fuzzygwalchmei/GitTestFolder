import mysql
import csv

csv_data = csv.reader('/Fuzzle/Documents/all_suppliers.csv')

database = mysql.connector.connect (database = "demodb", user="root@localhost", password="MySQLPassword", host="localhost", port="3306")

cursor = database.cursor()
delete = """Drop table if exists Real.SampleDataTwo"""
print (delete)

mydata = cursor.execute(delete)

cursor.execute("""Create Table Real.SampleDataTwo
                (User varchar(55),
                LastUpdate timestamp,
                Week date,
                Builder varchar(55),
                Traffic integer
                );""")

print("Table created successfully")

for row in csv_data:

    cursor.execute("INSERT INTO Real.SampleDataTwo (User, LastUpdate, Week, Builder, Traffic)"\
                "VALUES (%s,%s,%s,%s,%s)",
               row)


cursor.close()
database.commit()
database.close()

print ("CSV data imported")
