import os
import schedule
import time
import datetime
import sys

def DeleteEmptyFiles(Path):

    if not os.path.isdir(Path):
        print("Directory does not exist.")
        return

    with open("DeleteLog.txt", "a") as fobj:

        fobj.write("\n----------------------------------\n")
        fobj.write("Time : " +
                   datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                   "\n")

        for FolderName, SubDirectory, FileNames in os.walk(Path):

            for File in FileNames:

                FilePath = os.path.join(FolderName, File)

                try:

                    if os.path.getsize(FilePath) == 0:

                        os.remove(FilePath)

                        print(FilePath, "Deleted")

                        fobj.write(FilePath + "\n")

                except PermissionError:
                    print("Permission Denied :", FilePath)

                except Exception:
                    print("Unable to delete :", FilePath)

def main():

    if len(sys.argv) != 2:
        print("Usage : python Program.py Directory")
        return

    schedule.every(1).minutes.do(DeleteEmptyFiles, Path=sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()