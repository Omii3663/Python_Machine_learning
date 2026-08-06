import datetime
import schedule
import time


def filecreation(filename):
    TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    Full_fileName = f"{filename}_{TimeStamp}.txt"
    Date = datetime.datetime.now().strftime("%d_%m_%Y")
    Time = datetime.datetime.now().strftime("%H_%M_%S")

    try:
        with open(Full_fileName, "x") as f:
            f.write(f"File Name:{filename}_{TimeStamp}\n")
            f.write(f"Creation Date:{Date}\n")
            f.write(f"Creation Time:{Time}\n")
    except FileExistsError:
        print("File already exists")

def main():
    Name = input("Enter the file name:")
    filecreation(Name)

    schedule.every(1).minute.do(filecreation,filename=Name)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
