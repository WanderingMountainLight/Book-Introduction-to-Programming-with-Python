#Write a program that uses a multiply function to multiply two numbers and returns the result.
#Ask the user to enter the two numbers, then output the numbers and result as a simple equation.


def multiply(x, y):
    return x * y

#print(multiply(3,5.5))

def get_numbers(user_input):
    data = input(user_input)
    return float(data)


num1 = get_numbers("Enter first number:  ")
num2 = get_numbers("Enter second number:  ")

result = multiply(num1, num2)

print(f'{num1} * {num2} = {result}')

#Slowly getting better with syntax. Understanding the logic
#of what needs to happen, still working through the language
#to get the program to do what I want to accomplish.