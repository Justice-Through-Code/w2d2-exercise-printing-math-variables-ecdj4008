
def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
 fahrenheit = 100
 celsius_100 = (fahrenheit - 32) * 5/9
 print(celsius_100)
 print('int')
# I first convert 'farenheit' by subtracting -32 from it and multiplying it by '5/9'. All intergers are involved so it is an interger       
#convert_100_to_celsius()
fahrenheit = 0
celsius_0 = (fahrenheit - 32) * 5/9
print(celsius_0)


def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    fahrenheit = 0
    celsius_0 = (fahrenheit - 32) * 5/9
    print(celsius_0)


#convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    print((34.2 - 32) * 5/9)
#convert_34_2_to_celsius()


# Now, can you convert back?


def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    celsius = 5
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)
#convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    fahrenheit_to_celsius = (fahrenheit_temp - 32) * 5/9

    if celsius_temp > fahrenheit_to_celsius:
        print('30.2 degrees Celsius is hotter')
    else:
        print('85.1 degrees Fahrenheit is hotter')
#hotter_temp()
