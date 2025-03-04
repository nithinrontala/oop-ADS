class Clock:
    def __init__(self,*args):
        # print(len(args), args)
        if(len(args) == 2):
            if args[0]>24 or args[0]<0 or args[1]>60 or args[1]<=0:
                self.hrs = 0
                self.min = 0
            else:
                self.hrs = args[0]
                self.min = args[1]
        if(len(args) == 1):
            # print("hello")
            sp = args[0].split(":")
            if int(sp[0])>24 or int(sp[1])>60 or int(sp[0])< 0 or int(sp[1])<=0:
                self.hrs = 0
                self.min = 0
            else:
                self.hrs = int(sp[0])
                self.min = int(sp[1])
        
    def tic(self):
        self.min += 1
        if self.min == 60:
            self.min = 0
            self.hrs += 1
            if self.hrs == 24:
                self.hrs = 0

    def toc(self,min):
        self.min += min
        while self.min >= 60:
            self.min -= 60
            self.hrs += 1
            if self.hrs == 24:
                self.hrs = 0

    def isEarlier(self,time):
        # print("hi")
        if self.hrs < time.hrs:
            return True
        elif self.hrs == time.hrs and self.min < time.min:
            return True
        return False

    def toString(self):
        return f"{self.hrs:02d}:{self.min:02d}"


def main():
    type = input()
    testCases = input()
    testCases = int(testCases)
    while int(testCases)>0:

        if type == "constructor(String)":
            t = (input())
            obj = Clock(t)
            print(obj.toString())
        elif type == "constructor(int, int)":
            t = input().split(",")
            obj = Clock(int(t[0]),int(t[1]))
            print(obj.toString())
        elif type == "tic()":
            t = input()
            obj = Clock(t)
            obj.tic()
            print(obj.toString())
        elif type == "toc(int)":
            t = input().split(",")
            obj = Clock(t[0])
            obj.toc(int(t[1]))
            print(obj.toString())
        elif type == "isEarlierThan(Clock)":
            t = input().split(",")
            # print(t[0])
            clock1 = Clock(t[0])
            # print("hi")
            clock2 = Clock(t[1])
            if clock1.isEarlier(clock2):
                print("true")
            else:
                print("false")
        elif type == "toString()":
            print("null")
        testCases-=1
if __name__ == "__main__":
    main()