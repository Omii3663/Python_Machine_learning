import os
import datetime

def Display(Directory):
    DictNames = []
    NumOfFiles = 0
    DateTime = datetime.datetime.now()

    if (os.path.exists(Directory)):
        if(os.path.isdir):

            for FolderName, SubFolder, FileNames in os.walk(Directory):
            
                    for fname in FolderName:
                        DictNames.append(fname)
            
                    for filename in FileNames:
                        NumOfFiles += 1
        else:
             print("Its Not Directory")

    else:
         print("Directory/Folder does not Exits!")

    return DictNames, NumOfFiles, DateTime

def main():
     print("Enter Directory Path/name")
     dic = input("").strip()
     DictNames, NumOfFiles, DateTime = Display(dic)
     print(f"Directory Path : {dic}")
     print(f"Total Files : {NumOfFiles}")
     print(f"Date Time : {DateTime}")

if __name__ == "__main__":
     main()

    

        
