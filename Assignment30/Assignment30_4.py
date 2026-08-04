
import schedule
import time
import datetime
Border="-"*40
def Display():
    
    print("Namaskar ")
def main():
    print(Border)
    print("Task Scheduler Started... Press Ctrl+C to exit.")
    print(Border)
    
    schedule.every().day.at("09:00").do(Display)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped cleanly by user.")

if __name__ == "__main__":
    main()