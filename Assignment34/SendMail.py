import smtplib
import os
import datetime
from email.message import EmailMessage
from dotenv import load_dotenv
import sys



load_dotenv()


def sendMail(FilePath):

    # timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    flag=True
    
    print(sys.argv[2])
    sender_email=os.getenv("Sender_Email")
    print(sender_email)

    #app Password
    app_Password=os.getenv("Sender_Password")
    print("Pass app",app_Password)

    receiver_mail=sys.argv[2]

    subject=str("Duplicate Final Remove Report ")

    body=f"""Hello ,
    This is log File of All Process Running on the Server

    Please find Detailed log file Attached to this email


    Thank you
    Regards,
    Omkar Kolte
   """
    
    msg=EmailMessage()
    msg["from"]=sender_email
    msg["To"]= receiver_mail
    msg["Subject"]=subject

    print(FilePath,"This file Path")

    msg.set_content(body)
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
    fobj=open(FilePath,"rb")
    file_data=fobj.read()
    fobj.close()

    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename="Log.txt"
    )

    try:
        #step 5 login using gmail+App Password

        smtp.login(sender_email,app_Password)

        smtp.send_message(msg)
        print("Sucess, Mail Send Sucessfully")

       
    except Exception as eobj:
        print("This error ",eobj)
        
    finally:
        smtp.quit()
    
    
  