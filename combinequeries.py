import mysql.connector

""" mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="76321j"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) """

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="76321j",
  database = 'sql_store'
)

mycursor = mydb.cursor()

query1 = "SELECT order_id, status FROM orders WHERE status NOT IN (2, 3)" # 2 and 3 are shipped and delivered
query2 = "SELECT order_id, status FROM orders WHERE shipped_date IS NULL"

difference = '(' + query1 + ' EXCEPT ' + query2 + ')' + 'UNION'+'(' + query2 + ' EXCEPT ' + query1 + ')' # to check if both queries give the same results
mycursor.execute(difference)
myresult = mycursor.fetchall()
print(myresult) #should be and is empty