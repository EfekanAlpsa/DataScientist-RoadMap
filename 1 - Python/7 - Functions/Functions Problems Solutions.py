# Question 1 & 2 & 3 :
# ---------------------

def calculate_area(dimension1,dimension2,shape="triangle"):

    if shape=="triangle":
        area= 1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)

    elif shape=="rectangle":
        area= dimension1*dimension2 # Rectangle area is: Length*Width

    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None

    return area

def print_pattern(n):

    for i in range(n):
        s = ''
        for j in range(i+1):
            s += '*'
        print(s)


# Time to Try Functions

width = 40
length = 20
rectangleArea = calculate_area(width,length,"rectangle")
print("Area of Rectangle : ",rectangleArea)

base = 20
height = 10
triangleArea = calculate_area(base,height)  # It is already triangle , so we did not write again
print("Are of Triangle : ",triangleArea)

choice = int(input("Type Input of Pattern : "))
print_pattern(choice)

