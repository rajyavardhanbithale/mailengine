import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from os import path
import sys

def genscript(format_type,filename):
    if format_type == 'txt':
        dir = os.path.dirname(os.path.realpath(__file__))

        f = open(dir + '/txt_template.raw','r')
        
        if '.py' in filename:
            pass
        else:
            filename = filename + '.py'

        if path.exists(filename) == True:
            print('File exists')
            sys.exit(0)
        else:
            pass

        c = open(filename,'w')
        c.write(f.read())
        c.close()


    elif format_type == 'rtf':
        dir = os.path.dirname(os.path.realpath(__file__))
        
        f = open(dir + '/rtf_template.raw','r')
        
        if '.py' in filename:
            pass
        else:
            filename = filename + '.py'
        
        if path.exists(filename) == True:
            print('File exists')
            sys.exit(0)
        else:
            pass

        c = open('main.py','w')
        c.write(f.read())
        c.close()



def mail(port,server,sender_mail,receive_mail,password,message): 
    port = port  # For starttls
    smtp_server = server
    sender_email = sender_mail
    receiver_email = receive_mail
    password = password
    message = message

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('OK')


#margin:91px 0px 15px 101px;">Test Mail</h1
def sendmailrtf(port,server,sender_mail,receive_mail,password,message_html,subject):
    sender_email = sender_mail
    receiver_email = receive_mail
    password = password

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
  
    html = message_html
    part = MIMEText(html, "html")
    message.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print('OK')

