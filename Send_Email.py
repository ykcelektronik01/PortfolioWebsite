import smtplib,ssl
import os

def send_mail(message):
    host="smtp.gmail.com" #standart host
    port=465 # standart port

    username="yusufkoraycan@gmail.com"
    password=os.getenv("PASSWORD") #sistem degiskenlerini kullanarak password'a erisebiliyoruz.
    #windows'umuz baska yerde acik degilse buna erisemez kimse. Sadece biz erisebiliriz.
    #cok onemli!

    context=ssl.create_default_context()

    receiver="yusufkoraycan@gmail.com"




    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)


