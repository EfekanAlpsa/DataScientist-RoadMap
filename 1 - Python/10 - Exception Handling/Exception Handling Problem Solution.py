try:
    number1 = int(input("Enter a number : "))
    number2 = int(input("Enter another number : "))
    div = number1/number2
except:
    print("Division by 0 not accepted")

else:
    print("Division = ",div)

finally:
    print("Thanks!")