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


print_largest_odd()


# 2.4.1 Finger Exercise
import re # regular expression


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


print_birthyear()


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


print_x_times()