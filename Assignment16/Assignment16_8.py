def star(No):
    for i in range(No):
        print("*", end=" ")

def main():
    print("Enter a number:")
    Value = int(input())
    
    star(Value)

if __name__ == "__main__":
    main()