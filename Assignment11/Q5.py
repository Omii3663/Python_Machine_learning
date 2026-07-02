def Palindrome(no):
    rev = 0
    temp = no
    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10
    if temp == rev:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

def main():
    print('-'*30)
    print("------Palindrome Check ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    Palindrome(No)

if __name__ == "__main__":
    main()