class Demo:
    Value = 0

    def __init__(self,No1,No2):
        self.a = No1
        self.b = No2

    def Fun(self):
        print("Inside Fun()")
        print("No1 = ",self.a)
        print("No2 = ",self.b)
        print()

    def Gun(self):
        print("Inside Gun()")
        print("No1 = ",self.a)
        print("No2 = ",self.b)
        print()


def main():

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()

    
        