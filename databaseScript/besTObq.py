import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="noobaki32",
    database="covid19"
)

mycursor = mydb.cursor()

for i in range(0, 257):
    sql = 'UPDATE covid19 SET iso2 = "BQ"' + 'WHERE iso3 = "BES";'
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    break
