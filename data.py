import mysql.connector
mb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sofia1703",
  port= 3306,
  database="gasagency"
)
c = mb.cursor()
#query = 'create database gasagency'
#query ='create table user ( fullname varchar(50),number varchar(50),address varchar(50), username varchar(50), password varchar(50))'
#query ='create table admin ( employeeid varchar(50),employeename varchar(50), ausername varchar(50), apassword varchar(50))'
#query ='create table comp ( compusername varchar(50),usercontact varchar(50), usercomp varchar(50))'
query ='create table book'
mb.commit()
