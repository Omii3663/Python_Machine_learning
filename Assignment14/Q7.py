Divisible = lambda No : True if No % 5 == 0 else False

def main():
    print('-'*30)
    print("----Divisible Using lambda----")
    print('-'*30)

    print("Enter Number :")
    No = int(input())

    Ret = Divisible(No)
    print("The Number is Divisible by 5 :",Ret)

if __name__ == "__main__":
    main()