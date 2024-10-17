import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
#cursor.execute("create database database01") 
cursor.execute("show databases")
for x in cursor:
   print(x) 
cursor.execute("use database01") 
#cursor.execute("CREATE TABLE departments (department_id INT PRIMARY KEY,department_name VARCHAR(50))")
cursor.execute("show tables")
print("Number of tables in database :")
for x in cursor:
     print("\t",x) 
s="insert into departments values(%s,%s)"
t=(1,"harish")
#cursor.execute(s,t)
#connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid) 
cursor.execute("select * from departments")
result=cursor.fetchall()
print("Content in the python :")
for x in result:
   print("\t",x)
sql = "update departments set department_name='bala' where department_id=2;"
cursor.execute(sql)
connection.commit() 
cursor.execute("select * from departments")
result=cursor.fetchall()
print("Content in the python :")
for x in result:
   print("\t",x)
sql = "DELETE FROM departments WHERE department_id=3"
# cursor.execute(sql)
# connection.commit()
print(cursor.rowcount, "record(s) deleted")  
