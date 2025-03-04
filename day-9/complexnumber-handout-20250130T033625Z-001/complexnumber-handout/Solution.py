class ComplexNumber:
    def __init__(self, realPart=0, imagPart=0):
        self.realPart = realPart
        self.imagPart = imagPart

    def init(self, realPart, imagPart):
        self.realPart = realPart
        self.imagPart = imagPart
        print(f"Initialized: {self.to_string()}")

    def adds(self, num):
        self.realPart += num[0]
        self.imagPart += num[1]
        print(f"After addition: {self.to_string()}")

    def sub(self, num):
        self.realPart -= num[0]
        self.imagPart -= num[1]
        print(f"After subtraction: {self.to_string()}")

    def mul(self, num):
        realPart = self.realPart * num[0] - self.imagPart * num[1]
        imagPart = self.realPart * num[1] + self.imagPart * num[0]
        self.realPart = realPart
        self.imagPart = imagPart
        print(f"After multiplication: {self.to_string()}")

    def div(self, num):
        deno = num[0] ** 2 + num[1] ** 2
        if deno == 0:
            print("Error: Division by zero is not allowed.")
            return
        realPart = (self.realPart * num[0] + self.imagPart * num[1]) / deno
        imagPart = (self.imagPart * num[0] - self.realPart * num[1]) / deno
        self.realPart = realPart
        self.imagPart = imagPart
        print(f"After division: {self.to_string()}")

    def mod(self):
        modulus = (self.realPart**2 + self.imagPart**2) ** 0.5
        print(f"Modulus: {modulus}")

    def conj(self):
        self.imagPart = -self.imagPart
        print(f"Conjugate: {self.to_string()}")

    def to_string(self):
        if self.imagPart >= 0:
            return f"{self.realPart} + {self.imagPart}i"
        else:
            return f"{self.realPart} - {-self.imagPart}i"


def run():
    complexNumber = ComplexNumber()
    while True:
        try:
            inp = input().strip()
            if inp == "exit":
                break
            if inp.startswith("initialize "):
                inp = inp.split("initialize ")
                inp_nums = inp[1].split(",")
                inp_nums = [float(ele) for ele in inp_nums]

                realPart, imagPart = inp_nums[0], inp_nums[1]
                complexNumber.init(realPart, imagPart)

            elif inp.startswith("add "):
                inp = inp.split("add ")
                inp_nums = inp[1].split(",")
                num = [float(ele) for ele in inp_nums]
                # print(num)
                complexNumber.adds(num)

            elif inp.startswith("subtract "):
                inp = inp.split("subtract ")
                inp_nums = inp[1].split(",")
                num = [float(ele) for ele in inp_nums]
                # print(num)
                complexNumber.sub(num)

            elif inp.startswith("multiply "):
                inp = inp.split("multiply ")
                inp_nums = inp[1].split(",")
                num = [float(ele) for ele in inp_nums]
                # print(num)
                complexNumber.mul(num)

            elif inp.startswith("divide "):
                inp = inp.split("divide ")
                inp_nums = inp[1].split(",")
                num = [float(ele) for ele in inp_nums]
                # print(num)
                complexNumber.div(num)

            elif inp.startswith("modulus "):
                inp = inp.split("modulus ")
                inp_nums = inp[1].split(",")
                num = [float(ele) for ele in inp_nums]
                # print(num)
                complexNumber.mod()

            elif inp.startswith("conjugate "):
                inp = inp.split("conjugate ")
                inp_nums = inp[1].split(",")
                num = [float(ele) for ele in inp_nums]
                # print(num)
                complexNumber.conj()
        except EOFError:
            break


run()
