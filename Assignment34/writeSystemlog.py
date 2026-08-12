
import psutil
import time
import datetime

def systemLog(filePath):
    Border="-"*50
    listprocess=[]
    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=["pid","name","username","status"])
        listprocess.append(info)
    fobj=open(filePath,"a+")
   
    fobj.write(Border + "\n")
    fobj.write("Process Log\n")
    fobj.write("Log Time : " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
    fobj.write(Border + "\n\n")

    for process in listprocess:
        fobj.write("User Name : {}\n".format(process.get("username")))
        fobj.write("PID       : {}\n".format(process.get("pid")))
        fobj.write("Name      : {}\n".format(process.get("name")))
        fobj.write("Status      : {}\n".format(process.get("status")))

        fobj.write(Border + "\n")

    fobj.close()


    print(Border)
    print("End of Script")
    print(Border)


    