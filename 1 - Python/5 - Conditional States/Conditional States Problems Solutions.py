# Question 1 :
# -------------

us = ["austin", "dallas", "chicago"]
uk = ["london", "bristol", "liverpool"]
tr = ["istanbul", "bursa", "ankara"]

# 1.Write a program that asks user to enter a city name and it should tell which country the city belongs to

city = input("Enter City Name : ")

if city in us:
    print(f'{city} is in USA')
elif city in uk:
    print(f'{city} is in UK')
elif city in tr:
    print(f'{city} is in TR')
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")

# 2.Write a program that asks user to enter two cities and it tells you if they both are in same country or not

city1 = input("Enter City 1 : ")
city2 = input("Enter City 2 : ")

if city1 in us and city2 in us:
    print("Both cities are in us")
elif city1 in uk and city2 in uk:
    print("Both cities are in uk")
elif city1 in tr and city2 in tr:
    print("Both cities are in tr")
else:
    print("They don't belong to same country")

# Question 2 :
# -------------

#   I.Ask user to enter Systolic blood pressure & diastolic blood pressure values
#   II.If systolic pressure is higher than 140, print high blood pressure on the screen
#   III.If diastolic pressure is higher than 90, print high blood pressure on the screen

Systolic_blood_pressure =input("Please enter your Systolic blood pressure value : ")
diastolic_blood_pressure = input("Please enter your Diastolic blood pressure value : ")

Systolic_blood_pressure = float(Systolic_blood_pressure)
diastolic_blood_pressure = float(diastolic_blood_pressure)

if Systolic_blood_pressure > 140 or diastolic_blood_pressure > 90:
    print("High blood pressure")
elif Systolic_blood_pressure < 140 and diastolic_blood_pressure < 90:
    print("High blood pressure")
else:
    print("Your Blood Pressure Is Ok !")











