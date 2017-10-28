class Employee:

    def __init__(self, full_name = "fdsfs dsfs", position = None, salary = None):

        self.full_name = full_name
        self.position = position
        self.salary = salary

    def name (self):
        sub=' '
        d = self.full_name.find(sub)
        return self.full_name[0:d]

    def surname (self):
        sub=' '
        m = self.full_name.find(sub)
        return self.full_name[m:len(self.full_name)]

a = Employee()
a.full_name = "Nasty Test"
print (a.name())
#     def full_name (self):
#         f = self.name + " " + self.surname
#         return  f
#     def __str__(self):
#         return ("<Employee" + self.full_name )
#
# if __name__== "__main__":
#     pass