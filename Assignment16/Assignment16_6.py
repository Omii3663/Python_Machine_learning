def CheckPosNeg(No):
    if No > 0:
        print("It is a Positive Number")
    elif No < 0:
        print("It is a Negative Number")
    else:
        print("It is Zero")

def main():
    print("Enter a number:")
    Value = int(input())
    
    CheckPosNeg(Value)

if __name__ == "__main__":
    main()  
    