class Employee:

    def __init__(self,id,name,age,gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f'ID : {self.id} \n NAME : {self.name} \n AGE : {self.age} \n GENDER : {self.gender}')

emp = Employee(1, "Luna", 20, "Female")

emp.display()
