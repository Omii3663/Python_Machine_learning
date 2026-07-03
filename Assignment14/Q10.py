#largest = lambda a,b,c : max(a,b,c) Using max func 
largest = lambda No1,No2,No3 : No1 if (No1>No2 and No1>No3) else(No2 if No2>No3 else No3)

def main():
    print('-'*40)
    print("----largest Number Using lambda----")
    print('-'*40)

    print("Enter First Number :")
    No1 = int(input())
    print("Enter Second Number :")
    No2 = int(input())
    print("Enter Third Number :")
    No3 = int(input())

    Ret = largest(No1,No2,No3)
    print("The largest Number is :",Ret)

if __name__ == "__main__":
    main()