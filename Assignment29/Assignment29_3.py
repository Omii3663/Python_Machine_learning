import os
import sys

def Copied(fileName, NewFileName):
    if os.path.exists(fileName):
        fobj = open(fileName, "r")
        cobj = open(NewFileName, "w+")
        
        cobj.write(fobj.read())
        cobj.seek(0)
        Data = cobj.read()
        
        fobj.close()
        cobj.close()
        print("Success: File copied successfully.")
    else:
        print("Error: Source file does not exist.")

def main():
    # sys.argv[0] is the script name
    # sys.argv[1] should be the source file name
    # sys.argv[2] should be the new destination file name
    if len(sys.argv) == 3:
        source_file = sys.argv[1]
        destination_file = sys.argv[2]
        Copied(source_file, destination_file)
    else:
        print("Usage Error: Please provide both the source and destination file names.")
        print("Example: python script.py Demo.txt CopyOfDemo.txt")

if __name__ == "__main__":
    main()
