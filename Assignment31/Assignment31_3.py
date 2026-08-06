import os
import datetime

def Display(Directory):
    DictNames = []
    NumOfFiles = 0
    NumOfSubDirs = 0
    ScanTime = datetime.datetime.now()

    if (os.path.exists(Directory)):
        if(os.path.isdir):

            for FolderName, SubFolder, FileNames in os.walk(Directory):
            
                    for fname in FolderName:
                        DictNames.append(fname)
            
                    for subname in SubFolder:
                        NumOfSubDirs += 1
            
                    for filename in FileNames:
                        NumOfFiles += 1
        else:
             print("Its Not Directory")

    else:
         print("Directory/Folder does not Exits!")

    return DictNames, NumOfFiles, NumOfSubDirs, ScanTime

def main():
     print("Enter Directory Path/name")
     dic = input("").strip()
     DictNames, NumOfFiles, NumOfSubDirs, ScanTime = Display(dic)
     print(f"Directory Saccend : {dic}")
     print(f"Total Files : {NumOfFiles}")
     print(f"Total Subdirectories : {NumOfSubDirs}")
     print(f"Scan Time : {ScanTime}")

if __name__ == "__main__":
     main()

    

        
