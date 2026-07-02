def GradeSys(No):
    if No >= 75:
        print("Distinction")
    elif No >= 60:
        print("First Class")
    elif No >= 50:
        print("Second Class")
    elif No < 50:
        print("Fail")

def main():
    print('-'*30)
    print("------Grade System ------")
    print('-'*30)

    print("Enter Marks :")
    No = int(input())
    
    GradeSys(No)

if __name__ == "__main__":
    main()