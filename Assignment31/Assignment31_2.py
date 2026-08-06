import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    message = input("Enter Messages You Want to display : ")
    schedule.every(5).seconds.do(DisplayMessage,message = message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
