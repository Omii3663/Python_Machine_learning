import datetime

def DisplayDateTime():
    now=datetime.datetime.now()
    print("Current Date & Time is : ",now)

def main():
    DisplayDateTime()

if __name__=="__main__":
    main()