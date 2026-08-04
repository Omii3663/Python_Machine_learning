import sys
import os
import schedule
import time

Boreder = "-"*40

def display():
    print("Jay Ganesh....")
    print(Boreder)

def main():
    print(Boreder)

    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
