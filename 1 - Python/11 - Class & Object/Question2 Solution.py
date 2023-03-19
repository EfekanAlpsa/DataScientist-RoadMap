class Employee:

    def __init__(self,id,name,age,gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


    def display(self):
        print(f' ID : {self.id} \n NAME : {self.name} \n AGE : {self.age} \n GENDER : {self.gender} \n SALARY : {self.salary}')

    def calculate_salary(self):

        if self.age > 40:
            salary = 2100 * (self.age-18)
            salary += 4000

            return salary

        else:
            salary = 2100 * (self.age-18)

            return salary

person1_name = input("Enter Person Name : ")
person1_age = int(input("Enter Person Age : "))
person1_gender = input("Enter Person Gender : ")

person1 = Employee(1, person1_name, person1_age, person1_gender)

person2_name = input("Enter Person Name : ")
person2_age = int(input("Enter Person Age : "))
person2_gender = input("Enter Person Gender : ")

person2 = Employee(2, person2_name, person2_age, person2_gender)


print(f"{person1_name} SALARY IS : {person1.calculate_salary()}")
print(f"{person2_name} SALARY IS : {person2.calculate_salary()}")
