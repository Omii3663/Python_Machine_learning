EvenOdd  = lambda No : True if No % 2 !=0 else False

def main():
    print('-'*30)
    print("----EvenOdd Using lambda----")
    print('-'*30)

    print("Enter Number :")
    No = int(input())

    Ret = EvenOdd(No)
    print("The Number is Odd :",Ret)

if __name__ == "__main__":
    main()