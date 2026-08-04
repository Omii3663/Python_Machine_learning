class Circle:
    PI = 3.14

    def __init__(self,Redius,Area,Circumference):
        self.Redius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter Radius :")
        r = int(input())
        self.Redius = r

    def CalculateArea(self):
        self.Area = Circle.PI * self.Redius * self.Redius
        return self.Area
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Redius
        return self.Circumference
    
    def Display(self):
        print("Radius : ", self.Redius)
        print("Area : ", self.Area)
        print("Circumference : ", self.Circumference)

def main():
    cobj = Circle(0.0,0.0,0.0)
    cobj.Accept()
    cobj.CalculateArea()
    cobj.CalculateCircumference()
    cobj.Display()

if __name__ == "__main__":
    main()