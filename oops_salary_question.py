#Started with employee class and then defined instance variables in private with two underscores for accessing only in this class
class Employee:
    def __init__(self,name,employee_id,basic_salary):
        self.__name=name
        self.__employee_id=employee_id
        self.__basic_salary=basic_salary
#This is the required function for calculating the salary total mentioned from hra,bonus,basicsalary       
    def calculate_salary(self):
        HRA=0.2*self.__basic_salary
        bonus=0.1*self.__basic_salary
        total_salary=self.__basic_salary+HRA+bonus
        return total_salary
#This is the function for displaying the details mentioned and after displaying totalsalary we need to call the function since the totalsalary is local variable in the function which is called
    def display_details(self):
        print("Name:",self.__name)
        print("Employee ID:",self.__employee_id)
        print("Total Salary:",self.calculate_salary())
f=Employee("mahesh",1,1200)
f.display_details()