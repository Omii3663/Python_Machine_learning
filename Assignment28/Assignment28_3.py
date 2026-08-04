def main():
    try:
        Name=input("Enter File Name : ")
        fobj=open(Name,"r")
        Data=fobj.read()
        print(Data)
    except FileNotFoundError:
        print("File not found.")
if __name__=="__main__":
    main()