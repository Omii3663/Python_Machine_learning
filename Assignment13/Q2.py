def Area(r,pi=3.14):
    return pi * r * r

def main():
    print('-'*30)
    print("------Area Of Circle ------")
    print('-'*30)

    print("Enter Redius :")
    No = int(input())
    
    print("Area of Circle is :")
    Ret = Area(No)
    print(Ret)

if __name__ == "__main__":
    main()