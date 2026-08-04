class Arthmetic:
    def __init__(self, Value1, Value2):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter First Number :")
        self.Value1 = int(input())
        print("Enter Second Number :")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2


def main():
    aobj = Arthmetic(0,0)
    #bobj = Arthmetic(2, 3)
    aobj.Accept()
    print("Addition : ", aobj.Addition())
    print("Subtraction : ", aobj.Subtraction())
    print("Multiplication : ", aobj.Multiplication())
    print("Division : ", aobj.Division())

if __name__ == "__main__":
    main()