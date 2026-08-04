def main():
    name=input("Enter File Name : ")
    try:
        robj=open(name,"r")
        Data=(robj.readlines())
        print(f"Total Lines in {name} : {len(Data)}")
    except FileNotFoundError:
        print(f"File {name} not found.")    

if __name__=="__main__":
    main()