<<<<<<< HEAD
def Factorial(No):
    count = 1
    for i in range(1,No+1):
        count  = count *   i

    print(count)   
    
def main():
    print('-'*40)
    print("------Factorial of Number ------")
    print('-'*40)

    print("Enter Number :")
    No = int(input())
    print(f"The Factorial of {No}  is :")
    total = Factorial(No)

if __name__ == "__main__":
=======
def Factorial(No):
    count = 1
    for i in range(1,No+1):
        count  = count *   i

    print(count)   
    
def main():
    print('-'*40)
    print("------Factorial of Number ------")
    print('-'*40)

    print("Enter Number :")
    No = int(input())
    print(f"The Factorial of {No}  is :")
    total = Factorial(No)

if __name__ == "__main__":
>>>>>>> f0edf1d (Complete Assignment 10)
    main()