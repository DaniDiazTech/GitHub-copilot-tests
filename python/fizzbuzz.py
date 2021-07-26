# FizzBuzz function that receives a parameter "number"
# If the number is divisable by 3, print "Fizz"
# If the number is divisable by 5, print "Buzz"
# But if the number is divisable by 3 and 5 it prints "FizzBuzz"
# Else, print the number
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)