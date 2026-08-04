import schedule
import time
import datetime
Border="-"*40
def Display():
    fobj=open("Marvellous.txt","+a")
    timestamp=datetime.datetime.now()
    fobj.write(str(timestamp) + "\n")


    fobj.close()
def main():
   
    print(Border)
    
    schedule.every(1).minutes.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(45)
if __name__=="__main__":
    main()