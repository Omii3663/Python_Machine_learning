<<<<<<< HEAD
def PerfectNumber(No):
    Sum = 0 
    for i in range(1, No):
        if No % i == 0:
            Sum += i 
    if Sum == No:
        print(f"{No} is a Perfect Number")
    else:
        print(f"{No} is not a Perfect Number")

def main():
    print('-'*30)
    print("------Perfect Number Check ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    
    PerfectNumber(No)

if __name__ == "__main__":
=======
def PerfectNumber(No):
    Sum = 0 
    for i in range(1, No):
        if No % i == 0:
            Sum += i 
    if Sum == No:
        print(f"{No} is a Perfect Number")
    else:
        print(f"{No} is not a Perfect Number")

def main():
    print('-'*30)
    print("------Perfect Number Check ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    
    PerfectNumber(No)

if __name__ == "__main__":
>>>>>>> f82048f (ok)
    main()