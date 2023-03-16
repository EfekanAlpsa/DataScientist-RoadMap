# Question 1 :
# -------------

print("Question 1 \n")

animals = ["lion","tiger","tiger","pig","ping","lion","tiger","lion","tiger","pig"]
count = 0
for i in animals:
    if i == "pig":
        count+=1

print("Number of Pigs : ",count)

# Question 2 :
# -------------

print("Question 2 \n")

for i2 in range(1,11):
    if i2 % 2 != 0:
        print(i2 * i2)

# Question 3 :
# -------------

print("Question 3 \n")

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You did not spend {e} in any month')

# Question 4 :
# -------------

print("Question 4 \n")

for i in range(5):
    print(f"You ran {i+1} miles")  # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4:  # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

# Question 5 :
# -------------

print("Question 5 \n")

print("\nExercise 5\n")

for i in range(1,6):
    c = ''
    for j in range(i):
        c += '*'
    print(c)

# Question 6 :
# -------------

totalNumber = 0
number = int(input("Enter a number : "))

while number != 0:

    totalNumber += number
    number = int(input("Enter a number : "))

print("Total : ",totalNumber)


