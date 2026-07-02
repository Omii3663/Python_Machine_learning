def DigitSum(no):
    sum = 0
    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10
    print("Sum of digits is :",sum)

def main():
    print('-'*30)
    print("------Sum of Digits ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    DigitSum(No)

if __name__ == "__main__":
    main()
        
    
    