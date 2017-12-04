class Employee:
    empCunt =0
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
        Employee.empCunt+=1
    def displayCount(self):
        print 'Total employee %d '% Employee.empCunt

    def displayEmployee(self):
        print 'name:',self.name,",Salary:",self.salary

e = Employee('kk',1234)
e.displayEmployee()