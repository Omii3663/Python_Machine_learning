Power = lambda x : x ** 2

def main():
    num = int(input("Enter a number: "))
    result = Power(num)
    print(f"The square of {num} is {result}")

if __name__ == "__main__":
    main()