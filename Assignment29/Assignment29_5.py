import os
def Chkfrequency(fileName,find):
    try:
        if os.path.exists(fileName):
            fobj=open(fileName,"r")
            count=0
            for i in fobj:
                if find in i:
                    count=count+1
            print(f"Letter {find} is present {count} times in the file {fileName}")
            fobj.close()
        else:
            print(f"Error: The file '{fileName}' does not exist.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
def main():
    print("Enter File Name Which You Want To Search  : ")
    fileName=input()
    print(f"Enter Letter/String Which You Want To Search in {fileName} ")
    find=input()
    Chkfrequency(fileName,find)

if __name__=="__main__":
    main()