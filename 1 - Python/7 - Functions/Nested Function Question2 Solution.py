name = input("Enter Name : ")
age = int(input("Enter Age : "))
music = input("Enter Your Fav Music Name : ")

def func(*args):
    print(args)
    print(type(args))

func(name,age,music)