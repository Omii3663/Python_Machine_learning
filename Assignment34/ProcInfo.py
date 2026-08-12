import psutil
import schedule
import os

def getSystemLog():
    listOfProcess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])

        listOfProcess.append(info)

    Data = listOfProcess

    for process in Data:

        print(f"Name of the user is : {process['username']}  & Name of process is {process['name']} and PID is {process['pid']}")
        print("Name :%s\n"%process.get("username"))
        print("Process :%s\n"%process.get("process"))
        print("PID is :%s\n"%process.get("pid"))

def main():
    getSystemLog()

if __name__ == "__main__":
    main()

