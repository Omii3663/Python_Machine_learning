def CheckPrime(No):
    if No > 1 :
        for i in range(2,No):
            if No % i == 0:
                return False
            else:
                return True
            
def main():
    print("-"*25)
    print("  ----Check Prime----")
    print("-"*25)

    print("Enter Number :")
    No = int(input())

    Ret = CheckPrime(No)

    if Ret == True:
        print("The Number is Prime Number")
    else:
        print("The Number is Not Prime Number")


if __name__ == "__main__":
    main()
            
                


