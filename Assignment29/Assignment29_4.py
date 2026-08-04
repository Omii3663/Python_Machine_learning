import os
import sys
import hashlib

def CompareFile(FileOne ,FileTwo):
    
     fobj1=open(FileOne,"r+b")
     fobj2=open(FileTwo,"r+b")
     hobj1=hashlib.md5()
     hobj2=hashlib.md5()
     Buffer1=fobj1.read(1000)
     Buffer2=fobj2.read(1000)
     while(len(Buffer1)>0):
         hobj1.update(Buffer1)
         Buffer1=fobj1.read(1000)

     while(len(Buffer2)>0):
         hobj2.update(Buffer2)
         Buffer2=fobj2.read(1000)
     print(hobj1.hexdigest())
     print(hobj2.hexdigest())

     return (hobj1.hexdigest()==hobj2.hexdigest())


     
        
       

def main():
    if(len(sys.argv)==3):

        Ret=CompareFile(sys.argv[1],sys.argv[2])
        if(Ret):    
            print("Same File ")
        else:
            print("Different File ")
        
   
if __name__=="__main__":
    main()