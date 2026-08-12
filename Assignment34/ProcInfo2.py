import psutil
import os 
import schedule
import sys
def getSystemLog():
    if(len(sys.argv)==2):

        listprocess=[]
        for proc in psutil.process_iter():
            info=proc.as_dict(attrs=["pid","name","username"])


            listprocess.append(info)
    
        # psutil.Process("pid","name")
        Data=listprocess
        flag=False
        for process in Data:
            #if(process.get("name")==sys.argv[1]):
            if(process["name"]==sys.argv[1]):
                print("Following Below Process are Runnning :")        
                print(process)
                flag=True
            
        if(flag==False):
            print("Process is Not Prsent or running at this moment")
            
    else:
        print("Invaild Arugment or Process not Found")
        

def main():
   getSystemLog()
   
   

      
    
if __name__=="__main__":
    main()