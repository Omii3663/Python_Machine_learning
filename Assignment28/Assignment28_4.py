import os
def Copied(fileName, NewFileName):
    if(os.path.exists(fileName)):
        fobj=open(fileName,"r")

        cobj=open(NewFileName,"w+")
        cobj.write(fobj.read())
        cobj.seek(0)
        Data= cobj.read()
        #print(Data)
        fobj.close()
        cobj.close()
       
       
        print("Sucessss")
    else:
        print("File not Exist")

def main():
    print("Enter File Name Which You Want To Copy from  : ")
    fileName=input()
    print(f"EnterFile Name Which You Want To Create & Copy {fileName} ")
    NewFileName=input()
    Copied(fileName, NewFileName)

if __name__=="__main__":
    main()