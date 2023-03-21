name = input("Enter Name : ")
age = int(input("Enter Age : "))
music = input("Enter Your Fav Music Name : ")

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(Name=name,Age=age,Music=music)