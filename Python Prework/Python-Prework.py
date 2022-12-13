#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(username):
    print("Hello_" + username + "!")

hello_name("USERNAME")

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(number):
    while number <= 100:
        if number % 2 == 1:
            print(number)
            number += 1
            continue
        elif number == 100:
            return
        else:
            number += 1
            continue

first_odds(0           )

#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    digits = [1, 4, 12, 13, 5, 8, 7]
    print(max(digits))

max_num_in_list("digits")

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_consecutive(a_list):
    year = input("Write a year: ")
    if int(year)%4 == 0:
        print("True")
    elif int(year)%100 != 0 and int(year)%400 == 0:
        print("True")
    else:
        print("False")

is_consecutive("year")


#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(numbers):

    if sum(numbers) == ((len(numbers))/2) * (int(numbers[0]) + int(numbers[-1])):
        print("True")
    else:
        print("False")

is_consecutive([1, 2, 3, 4, 6])
