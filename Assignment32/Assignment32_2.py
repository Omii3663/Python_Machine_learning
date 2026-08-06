import datetime
import os
import schedule
import sys
import time

def FileSize(Directory):
    now = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    if (os.path.isfile(Directory)):
        Size = os.path.getsize(Directory)
        with open("FileSize.txt", "a+") as f:
            f.write(f"File Name:{Directory}\n")
            f.write(f"File Size:{Size} bytes\n")
            f.write(f"Timestamp:{now}\n")
            f.write("----------------------------\n")
    else:
        print("File is under Creation")
        print("File is Created  Sucessfully")
        fobj=open("FileSizeLog.txt", "a")
        fobj.write(f"File Path : {Directory}\n")
        fobj.write("File does not exist.\n")
        fobj.write(f"Date & Time : {now}\n")
        fobj.write("--------------------------------------\n")

def main():
      if(len(sys.argv)==2):
            schedule.every(30).seconds.do(FileSize,Directory=sys.argv[1])
      else:
            print("Please provide the file name as a command line argument")

      while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()   

    
