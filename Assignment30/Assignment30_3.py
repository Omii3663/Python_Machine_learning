import os
import time
import schedule

def Display():
    print("Jay Ganesh....")
    print("-"*40)

def main():
    print("-"*40)

    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()