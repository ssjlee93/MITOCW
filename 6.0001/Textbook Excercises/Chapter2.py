import re  # regular expression
import sys


# 2.3 Finger Exercise
# The book has not covered any loop yet. so I used plain if statements
def print_largest_odd():
    candidates = []
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    if x % 2 != 0:
        candidates.append(x)
    if y % 2 != 0:
        candidates.append(y)
    if z % 2 != 0:
        candidates.append(z)

    if len(candidates) == 0:
        print(min(x, y, z))
    else:
        print(max(candidates))


# 2.4.1 Finger Exercise


def print_birthyear():
    pattern = re.compile("^[1-9]{1,2}/[1-9]{1,2}/[1-9]{4}")
    birthday = input("Enter your birthday (mm/dd/yyyy) ")
    if pattern.match(birthday) is not None:
        divided = birthday.split("/")
        month = int(divided[0])
        if month < 1 or month > 12:
            return print("Invalid month")
        day = int(divided[1])
        if day < 1 or day > 31:
            return print("Invalid day")
        year = int(divided[2])
        return print("You were born in the year", year)
    else:
        return print("Incorrect format", birthday)


# 2.5 Finger Exercise


def print_x_times():
    num_x = int(input('How many times should I print the letter X? '))
    if num_x < 0:
        return print("Invalid input. Enter a positive input")
    to_print = ''
    num_iteration = 0
    while num_iteration < num_x:
        to_print += 'X'
        num_iteration += 1
    print(to_print)


# 2.5 Finger Exercise 2


def print_largest_odd_w_while():
    largest_odd = -sys.maxsize - 1
    num_iteration = 0
    while num_iteration < 10:
        user_input = int(input("Enter an integer "))
        if user_input % 2 != 0:
            largest_odd = max(largest_odd, user_input)
        num_iteration += 1
    if largest_odd == -sys.maxsize - 1:
        return print("No odd integer found")
    else:
        return print("The largest odd integer out of 10 inputs is:", largest_odd)


# 2.6 Finger Exercise


def find_prime_numbers(limit):
    primes = [2]
    for i in range(3, limit):
        for j in range(len(primes)):
            if i % primes[j] == 0:
                break
            if j == len(primes)-1:
                primes.append(i)
    print(primes)


# executions
# print_largest_odd()
# print_birthyear()
# print_x_times()
# print_largest_odd_w_while()
find_prime_numbers(1000)

