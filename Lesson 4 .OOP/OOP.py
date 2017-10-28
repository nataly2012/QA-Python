class Employee:
    # named = "somename"
    # typed = "sometype"
    def __init__(self, name = None, surname = None, position = None, salary = None):
        self.name = name
        self.surname = surname

        self.position = position
        self.salary = salary

    def income (self, month):
        i = month * self.salary
        return i

    def full_name (self):
        f = self.name + " " + self.surname
        return  f
    def __str__(self):
        return ("<Employee" + self.full_name )

if __name__== "__main__":
    pass
#значения класса не выводятся при наследовании

print(full_name("dsad dsada"))
