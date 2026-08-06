import os
import datetime
import shutil
import sys
import time
import schedule

def CopyFiles(Source, Destination):
    if not os.path.exists(Source):
        print(f"{Source} : Source file/Directory does not exists")
    elif not os.path.exists(Destination):
        print(f"{Destination} :Destination file/Directory does not exists")

    with open("copylog.txt","a") as f:
        f.write("\n---------------------------------\n")
        f.write("Time :" + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")+"\n")

        for FolderName, SubFolderName, FileName in os.walk(Source):
            for File in FileName:
                if File.endswith(".txt"):
                    SourcePath = os.path.join(FolderName,File)

                    try:
                        shutil.copy2(Source,Destination)
                        print(File, "Copied")
                        f.write(SourcePath + "n")

                    except Exception as e:
                        print("Connot Copy FIles..",e)

def main():
    if(len(sys.argv)!=3):
        print("Usage : python pythonProgram.py Source Distination")

    schedule.every(10).minute.do(
        CopyFiles,
        Source = sys.argv[1],
        Destination = sys.argv[2]
    )

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

