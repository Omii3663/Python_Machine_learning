import os
def toFind(fileName,find):
    if os.path.exists(fileName):
        fobj=open(fileName,"r")
        
        for i in fobj:
            if(find in i):
                print(f"Found the Letter {find} in the file {fileName}")
                break
            else:
                print(f"Letter {find} not found in the file {fileName}")
                break

    fobj.close()
         
                
         

   
def main():
    print("Enter File Name Which You Want To Search  : ")
    fileName=input()
    print(f"Enter Letter Which You Want To Search in {fileName} ")
    find=input()
    toFind(fileName,find)

if __name__=="__main__":
    main()