def Reverse(no):
    reverse = 0
    while no > 0:
        digit = no % 10
        reverse = reverse * 10 + digit
        no = no // 10
    print("Reverse of the number is :", reverse)

def main():
    print('-'*30)
    print("------Reverse of a Number ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    Reverse(No)

if __name__ == "__main__":
    main()
        
    
    