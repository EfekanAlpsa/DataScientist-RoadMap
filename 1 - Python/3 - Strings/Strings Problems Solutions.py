# Question 1 :
# -------------

street = "5th avenue"
city = "New York"
country = "US"
address = street + '\n' + city + '\n' + country
print("Address Using + Operator : ",address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string : ",address)

# Question 2 :
# -------------

s = "Earth Revolves Around The Sun"
print(s[6:14])
print(s[-3:])

# Question 3 :
# -------------

fruits = 5
veggies = 6
print(f"I eat {fruits} fruits and {veggies} daily")

# Question 4 :
# -------------

s = 'I want 2000 banana'
s = s.replace("banana","computer")
s = s.replace("2000","10")
print("Using Two Line Replace : ",s)

s = 'I want 2000 banana'
s = s.replace("banana","computer").replace("2000","10")
print("Using Single Line : ",s)






