def Area(length,width):
    return length * width

def main():
    print('-'*30)
    print("------Area Of Rectangle ------")
    print('-'*30)

    print("Enter Length of Rectangle :")
    No1 = int(input())

    print("Enter Width of Rectangle :")
    No2 = int(input())
    
    print("Area of Rectangle is :")
    Ret = Area(No1, No2)
    print(Ret)

if __name__ == "__main__":
    main()