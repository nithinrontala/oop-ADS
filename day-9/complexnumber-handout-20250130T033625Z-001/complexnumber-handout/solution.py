class Complex_Number:
    def __init__(self):
        self.real = 0.0
        self.imaginary = 0.0

    def initialize(self,num):
        num = num.split(",")
        self.real = float(num[0])
        self.imaginary = float(num[1])
        # print(self.real)
        print(f"Initialized: {self.tostring()}")

    def add(self,num):
        num = num.split(",")
        # print(num)
        self.real = self.real + float(num[0])
        self.imaginary = self.imaginary + float(num[1])
        print(f"After addition: {self.tostring()}")

    def subtract(self,num):
        num = num.split(",")
        self.real = self.real - float(num[0])
        self.imaginary = self.imaginary - float(num[1])
        print(f"After subtraction: {self.tostring()}")

    def multiply(self,num):
        num = num.split(",")
        real = (self.real * float(num[0])) - (self.imaginary * float(num[1]))
        imaginary = (self.real *float(num[1])) + (self.imaginary * float(num[0]))
        self.real = real
        self.imaginary  = imaginary
        print(f"After multiplication: {self.tostring()}")

    def divide(self, num):
        num = num.split(",")
        # print(num[0], num[1])
        num[0] = float(num[0])
        num[1] = float(num[1])
        denominator = num[0] ** 2 + num[1] ** 2
        # print(denominator)
        if denominator == 0:
            print("Error: Division by zero is not allowed.")
        else:
            real = (self.real * num[0] + self.imaginary * num[1]) / denominator
            imaginary = (self.imaginary * num[0] - self.real * num[1]) / denominator
            self.real = real
            self.imaginary = imaginary
            print(f"After division: {self.tostring()}")

    def modulus(self,num):
        num = num.split(",")
        # print(self.real, self.imaginary)
        a = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        print(f"Modulus: {a}")
    
    def conjugate(self,num):
        self.imaginary = - self.imaginary
        # print(self.tostring())
        print(f"Conjugate: {self.tostring()}")

    def tostring(self):
        # print(self.imaginary)
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"

    def complexManipulation(self):
        while True:
            try:
                s = input().split()
                if s[0] == "initialize":
                    self.initialize(s[1])
                elif s[0] == "add":
                    self.add(s[1])
                elif s[0] == "subtract":
                    self.subtract(s[1])
                elif s[0] == "multiply":
                    self.multiply(s[1])
                elif s[0] == "divide":
                    self.divide(s[1])
                elif s[0] == "modulus":
                    self.modulus(s[1])
                elif s[0] == "conjugate":
                    self.conjugate(s[1])
            except:
                break

if __name__ == "__main__":
    c = Complex_Number()
    c.complexManipulation()
    