from functools import reduce
Multiplication = lambda a,b : a * b

def main():
    lst = [10,45,12,4,5,78,32,]
    print("Input Data :",lst)

    Rdata = reduce(Multiplication,lst)
    print("Product of Data",Rdata)

if __name__ == "__main__":
    main()

