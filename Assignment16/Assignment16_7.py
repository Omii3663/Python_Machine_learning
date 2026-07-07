def IsDivisileBy5(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter a number:")
    Value = int(input())
    
    Ret = IsDivisileBy5(Value)
    if Ret == True:
        print("It is Divisible by 5")
    else:
        print("It is Not Divisible by 5")

if __name__ == "__main__":
    main()
    