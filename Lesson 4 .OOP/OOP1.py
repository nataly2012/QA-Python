from OOP import Employee

class ITEmpl(Employee):
    # def __init__(self, name = None, surname = None, position = None, salary = None):
    #     Employee.__init__(self, name, surname, position, salary)
        # self.name = name
        # self.surname = surname
        # self.position = position
        # self.salary = salary

    #Оптимизируем! ))
    def __init__(self,*args,**kwargs):
        # Employee.__init__(self,*args,**kwargs)
        # self.skills = []
        super().__init__(*args,**kwargs) #базовый класс
        self.skills = []

    def add_skill(self,skill):
        self.skills.append(skill)
#
if __name__== "__main__":
    empl = ITEmpl()
    empl.add_skill("Python")
    empl.add_skill("git")
    print(empl.skills)