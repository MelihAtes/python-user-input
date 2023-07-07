# python user input

name = input("What is your name?: ")
# int is for integers
age = int(input("How old are you?: "))
# float is for floating-point numbers or decimal numbers
# it is not working if your write "178,5" like me. You must write with a period(178.5), not a comma(178,5).
height = float(input("How tall are you?: "))


print("Hello there "+name+" !")
# Str is for converting the numbers of height and age commands into strings to display them separately.
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")
print("You are going to be "+str(age + 1)+" years old next year")