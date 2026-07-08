def Pattern(No):
    for i in range(No+1):
        for j in range(No+1):
            print("*", end=" ")
        print()

def main():
    print("Enter a number:")
    Value = int(input())
    
    Pattern(Value)

if __name__ == "__main__":
    main()
