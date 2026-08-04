def main():
    name=input("Enter File Name : ")
    try:
        robj=open(name,"r")
        Data=(robj.read())
        words=Data.split()
        print(f"Total Words in {name} : {len(words)}")
    except FileNotFoundError:
        print(f"File {name} not found.")

if __name__=="__main__":
    main()
    