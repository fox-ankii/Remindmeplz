import sqlite3
import random
import datetime
from datetime import date
from simplegmail import Gmail

gmail = Gmail()

today = date.today()

print (today.day,today.month,today.year)

print(today)


x=input("please provide date")
y=input("please provide month")
z=input("please provide year")
xx=input("Please share what is the event")

connection = sqlite3.connect("ridhi.db")
cursor = connection.cursor()
#cursor.execute("CREATE TABLE calendra( day int , mnth int , year int, evnt text)");
#cursor.execute('INSERT INTO application20 VALUES(?,?)'(input2,bucket))
cursor.execute("INSERT INTO calendra VALUES ( ?,?,?,? )", (x,y,z,xx));
connection.commit()

datetime1 = date.strftime(today,'%m,%d,%Y')
print(datetime1)
datetime2 = date.strftime(today,'%d')
print(datetime2)
datetime3 = date.strftime(today,'%m')
print(datetime3)
datetime4 = date.strftime(today,'%m')
print(datetime4)

yy = xx



aa = [1,2,3,4,5,6,7,8,9,0]
bb = [1,2,3,4,5,6,7,8,9,0]
cc = [1,2,3,4,5,6,7,8,9,0]
dd = [1,2,3,4,5,6,7,8,9,0]
ee = [1,2,3,4,5,6,7,8,9,0]

rndm = str(random.choice(aa))+str(random.choice(cc))+str(random.choice(dd))+str(random.choice(ee))
rndm1 = str(rndm)
cursor.execute("SELECT evnt FROM calendra WHERE day=(?)",(x,))
ans = cursor.fetchall()
print(ans)

abc = "agarwal123ridhi@gmail.com"
mudita = "Your OTp for login is "+ rndm1

while True :
 if datetime2 == x:
  params = {
  "to":   abc,
  "sender": "ankitagarwal333@gmail.com",
  "subject": "Your OTP is enclosed",
  "msg_html": mudita,
  "msg_plain": "Hi\nThis is a plain text email.",
  "signature": True  # use my account signature
 }
  message = gmail.send_message(**params)
 



   #print("huury up",xx) 
   #gmail = Gmail() # will open a browser window to ask you to log in and authenticate
 
   