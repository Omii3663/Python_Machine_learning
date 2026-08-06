import os
import sys
import schedule
import time

def Display(filename):
    try:
        if not os.path.exists(filename):
            print("file does not exits")
        elif not os.path.isfile(filename):
            print("Invaild file")
        elif not (os.path.getsize(filename)==0):
            print("file is Empty")

        with open(f"{filename}","r") as f:
            print(f.read())

    except PermissionError:
        print("Permission is denied")

    except OSError:
        print("file cannot be open")

def main():
    if(len(sys.argv)!=2):
        print("Invaild Arguments please Specify filename Also!!")
        return

    schedule.every(1).minute.do(Display,filename=sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()