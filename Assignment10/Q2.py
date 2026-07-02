<<<<<<< HEAD
def Sum(No):
    sum = 0
    for i in range(1,No+1):
        sum  = sum + i

    print(sum)   
    
def main():
    print('-'*40)
    print("------Sum Of N natural number ------")
    print('-'*40)

    print("Enter Number :")
    No = int(input())
    print(f"Sum of First  {No} Natural Number is :")
    total = Sum(No)

if __name__ == "__main__":
=======
def Sum(No):
    sum = 0
    for i in range(1,No+1):
        sum  = sum + i

    print(sum)   
    
def main():
    print('-'*40)
    print("------Sum Of N natural number ------")
    print('-'*40)

    print("Enter Number :")
    No = int(input())
    print(f"Sum of First  {No} Natural Number is :")
    total = Sum(No)

if __name__ == "__main__":
>>>>>>> f0edf1d (Complete Assignment 10)
    main()