import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("localhost","root","root","mysql")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s" % data)

db.close()