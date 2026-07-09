mult = lambda x,y : x * y

def main():
    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ret = mult(No1,No2)
    print(f"Multiplcation of {No1} x {No2} is : {Ret}")

if __name__ == "__main__":
    main()
    
