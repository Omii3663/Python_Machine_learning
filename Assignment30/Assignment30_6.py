import time
import schedule #use 24 hr formate

def Lunch():
    print("Lunch time!")

def Work():
    print("Wrap up Work")

def main():
    schedule.every().day.at("13:00").do(Lunch)  # Schedule lunch at 1:00 PM
    schedule.every().day.at("18:00").do(Work)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
