# Albert Alcaide Morales
# Date: February 13, 2023

#Program 1: Prints "Hello Word!", 100 times throught a for loop
print("\n\nProgram 1: ")
for i in range(100):    
    print("Hello World!")

# Program 2: Prints the integers on the list on a new line, in addition the square of each number on a new line
print("\n\nProgram 2: ")
for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(i)
    print(i**2)

# Program 3: Draws polygon and fills shape, with user input.
print("\n\nProgram 3: ")
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
x = input("Color of the outline?")    # user input for  turtle color
y = input("Color of filled?")         # input for fill color
tess.color(x)
tess.fillcolor(y)
tess.begin_fill()
n_str = input("How many sides? ")
n = int(n_str)
d_str = input("length of sides? ")
d = int(d_str)
for i in range(n):
    tess.forward(d)
    tess.left(360/n)
tess.end_fill() 
wn.exitonclick()

# Program 4: Program that has an iteration 1-50, that output if it divisble by 3, 5 ,or both
print("\n\nProgram 4: ")
for i in range(1, 51):         # range between 1-51, 51 because of n-1 at the end of range
    if i % 3 == 0 and i % 5 == 0:                   # if statement for divsible by both number needs to come first 
        print((i),"is divisible by 3 and 5")
    elif i % 3 == 0:
        print((i), "is divisible by 3")
    elif i % 5 == 0:
        print((i), "is divisible by 5")

# Program 5: Drawing picture with turtle module
print("\n\nProgram 5: ")
import turtle
wn = turtle.Screen()
wn.bgcolor("Black")
Z = turtle.Turtle()
Z.speed(20)
Z.color("red")
for i in range(700):
    Z.backward(i)
    Z.left(275)
    Z.right(60)
wn.exitonclick()