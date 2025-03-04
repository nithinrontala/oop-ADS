class DateADT:
    def __init__(self,*args):
        if len(args) == 3:
            self.year = int(args[0])
            self.month = int(args[1])
            self.day = int(args[2])
            self.hrs = 0
            self.mins = 0
            self.sec = 0
            self._validate_month()
            self._validate_day()
            self._validate_time()

        elif len(args) == 6:
            self.year = int(args[0])
            self.month = int(args[1])
            self.day = int(args[2])
            self.hrs = int(args[3])
            self.mins = int(args[4])
            self.sec = int(args[5])
            self._validate_month()
            self._validate_day()
            self._validate_time()
        
        elif isinstance(args[0],str):
            date_str = args[0]
            a = date_str.split()
            date_part = a[0]
            time_part = a[1]
            b = date_part.split('-')
            year = int(b[0])
            month = int(b[1] )
            day = int(b[2])
            c= time_part.split(':')
            hours = int(c[0])
            minutes = int(c[1])
            seconds = int(c[2])
            self.year = year
            self.month = month
            self.day = day
            self.hrs = hours
            self.mins = minutes
            self.sec = seconds
            self._validate_month()
            self._validate_day()
            self._validate_time()

    def _validate_month(self):
        if not (0 <= self.month <= 11):
            raise ValueError()

    def _validate_day(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[1] = 29
        if not (1 <= self.day <= days_in_month[self.month]):
            raise ValueError()

    def _validate_time(self):
        if not (0 <= self.hrs <= 23):
            raise ValueError()
        if not (0 <= self.mins <= 59):
            raise ValueError()
        if not (0 <= self.sec <= 60):
            raise ValueError()

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)


    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
    
    def getMinutes(self):
        return self.mins
    
    def getSeconds(self):
        return self.sec
    
    def getHours(self):
        return self.hrs
    
    def getTime(self):
        ms_per_day = 86400000
        ms = (self.year - 1970) * 365 * ms_per_day
        
        ms += self.month * 30 * ms_per_day
        
        ms += (self.day - 1) * ms_per_day
        
        ms += self.hrs * 3600000
        ms += self.mins * 60000
        ms += self.sec * 1000
        
        return ms
    
    def setTime(self, ms):
        ms_per_day = 86400000
        total_days = ms // ms_per_day
        remaining_ms = ms % ms_per_day

        self.year = 1970 + total_days // 365
        total_days %= 365

        self.month = total_days // 30
        total_days %= 30

        self.day = total_days + 1
        
        remaining_seconds = remaining_ms // 1000
        self.hrs = remaining_seconds // 3600
        remaining_seconds %= 3600
        self.mins = remaining_seconds // 60
        self.sec = remaining_seconds % 60

    def before(self,d2):
        if self.getYear() < d2.getYear():
            return True
        elif self.getYear() == d2.getYear():
            if self.getMonth() < d2.getMonth():
                return True
            elif self.getDay() < d2.getDay():
                return True
        return False
    
    def after(self,d2):
        return not self.before(d2)

    def setYear(self, year):
        self.year = year

    def setMonth(self, m):
        self.month = m

    def setDay(self,d):
        self.day = d

    def setHours(self,hrs):
        self.hrs = hrs
    
    def setMinutes(self,min):
        self.mins = min
    
    def setSeconds(self,sec):
        self.sec = sec
    
    def toString(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hrs:02d}:{self.mins:02d}:{self.sec:02d}"