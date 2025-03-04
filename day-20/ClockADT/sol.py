class Clock:
    def __init__(self, *args):
        if len(args) == 2:
            self.hrs = args[0]
            self.min = args[1]
            if not (0 <= self.hrs < 24 and 0 <= self.min < 60):
                self.hrs = 0
                self.min = 0
        elif len(args) == 1:
            time_str = args[0]
            sp = time_str.split(":")
            self.hrs = int(sp[0])
            self.min = int(sp[1])
            if not (0 <= self.hrs < 24 and 0 <= self.min < 60):
                self.hrs = 0
                self.min = 0

    def tic(self):
        self.min += 1
        if self.min == 60:
            self.min = 0
            self.hrs += 1
            if self.hrs == 24:
                self.hrs = 0

    def toc(self, minutes):
        self.min += minutes
        while self.min >= 60:
            self.min -= 60
            self.hrs += 1
            if self.hrs == 24:
                self.hrs = 0

    def isEarlier(self, time):
        if self.hrs < time.hrs:
            return True
        elif self.hrs == time.hrs and self.min < time.min:
            return True
        return False

    def toString(self):
        return f"{self.hrs:02d}:{self.min:02d}"


def main():
    clock_type = input().strip()
    testCases = int(input().strip())

    clock = None  # Initialize clock to None at the start

    while testCases > 0:
        if clock_type == "constructor(String)":
            t = input().strip()
            clock = Clock(t)
            print(f"{clock.toString()}")
        elif clock_type == "constructor(int, int)":
            t = input().strip()
            t = t.replace(',', ' ')
            hours, minutes = map(int, t.split())
            clock = Clock(hours, minutes)
            print(f"{clock.toString()}")
        elif clock_type == "tic()":
            if clock is not None:
                clock.tic()
                print(f"{clock.toString()}")
            else:
                print("No clock created yet.")
        
        testCases -= 1


if __name__ == "__main__":
    main()
