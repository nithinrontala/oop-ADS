class Employee:
    def __init__(self, empid, name, hr):
        self.employeeID = empid
        self.name = name
        self.hourlyRate = hr

    def calculatePay(self, hw):
        return self.hourlyRate * hw
    
class Payroll:
    def __init__(self, employees):
        self.employees = {}
        for emp in employees:
            self.employees[emp.employeeID] = emp

    def processPayroll(self, hm):
        pr = {}
        for k, v in hm.items():
            if k in self.employees:
                pr[k] = self.employees[k].calculatePay(v)
            else:
                pr[k] = "Employee not found"
        return pr

def main():
    emp1 = Employee(1, "Alice", 20.0)
    emp2 = Employee(2, "Bob", 25.0)
    emp3 = Employee(3, "Charlie", 30.0)
    
    payroll = Payroll([emp1, emp2, emp3])  

    hours_map = {1: 40.0, 2: 35.0, 3: 0.0}
    
    pay_results = payroll.processPayroll(hours_map)

    print("Payroll results:")
    for k, pay in pay_results.items():
        print(f"Employee ID {k} earned: {pay}")

if __name__ == '__main__':
    main()
