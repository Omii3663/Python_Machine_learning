import datetime
import schedule
import time

safe_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def fileCreation():
    try:
        fobj = open(f"Marvellouslog{safe_timestamp}.txt", "a+")
        fobj.write("Log file created successfully\n")
        fobj.write(f"Creation time: {safe_timestamp}")
        fobj.close()
    except FileExistsError:
        print("File already exists")

def main():

    schedule.every(1).seconds.do(fileCreation)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
