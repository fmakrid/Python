import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="noobaki32",
    database="covid19"
)

mycursor = mydb.cursor()


with open('iso2.txt', 'r') as iso2:
    with open('iso3.txt', 'r') as iso3:
        for selector in iso2:
            for selector2 in iso3:
                sql = 'UPDATE covid19 SET iso2 = '+'"' + selector.rstrip() + '"' + 'WHERE iso3 = '+'"' + selector2.rstrip() + '"'
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
                break