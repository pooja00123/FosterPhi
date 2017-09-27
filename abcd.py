
f_name=input("First Name: ")
l_name=input("Last Name: ")
e_m=input("Enter e-mail: ")
p=input("Password: ")
c_p=input("Confirm Password: ")
p_n=int(input("Phone Number: "))
g=input("gender: ")
print(f_name)
print(l_name)
print(e_m)
print(p)
print(c_p)
print(p_n)
print(g)
print("------------------------------log_in--------------------------------")
a=1
while(a==1):
	ee_m=input("enter e-mail id: ")
	p_=input(" enter password: ")
	if(e_m != ee_m or  p != p_):
  	  print("oops...!!!   wrong e-mail or password  ")
	else:
	 a=-1 
	 print(f_name,"  you are successfully signed in  ")


print("  <~><~>.....enjoy working with fosterphi....<~><~>  ")
import mysql.connector
from mysql.connector import Error

def connect():
	try:
		conn = mysql.connector.connect(host='localhost',database='record',user='root',password='pooja')
		if conn.is_connected():
			print('connected to mysql database')
	except Error as e:
		print(e)
	finally:
		conn.close()
if _name_ == '_main_' :
	connect()
