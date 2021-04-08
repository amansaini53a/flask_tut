class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        if self.first is None or self.last is None:
            print("Email is not set, Please set using setter")
        return f'{self.first}.{self.last}.@email.com'

    @email.setter
    def email(self, string):
        print("Setter called")
        name = string.split('@')[0]
        self.first = name.split(".")[0]
        self.last = name.split(".")[1]

    @email.deleter
    def email(self):
        self.first = None
        self.last = None


emp1 = Employee("aman", "saini")
print(emp1.email)
emp1.first = "Rogers"
print(emp1.email)

emp1.email = "aman.sharma@gmail.com"
print(emp1.email)



