def ChkNum(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter a number:")
    Value = int(input())
    
    Ret = ChkNum(Value)
    if Ret == True:
        print("It is an Even Number")
    else:
        print("It is an Odd Number")

if __name__ == "__main__":
    main()