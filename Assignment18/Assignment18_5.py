from MarvellousNum import ChkPrime


def ListPrime(Data):
    Sum = 0

    for Value in Data:
        if ChkPrime(Value):
            Sum += Value
    
    return Sum



def main():
    Size = int(input("How many numbers do you want to Enter?"))
    lst = []
    print("Enter the numbers:")
    for i in range(Size):
        No = int(input())
        lst.append(No)

    Result = ListPrime(lst)
    print("Addition of Prime Numbers is : ", Result)


if __name__ == "__main__":
    main()