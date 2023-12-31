import random


# 3.2 Finger Exercise 1
# the code will run endlessly
#   seems like I was correct

def square_root(x):
    epsilon = 0.01
    num_guesses, low = 0, 0
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**2 - x) >= epsilon:
        print("low =", low, "high =", high, "ans =", ans)
        num_guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print("number of guesses =", num_guesses)
    print(ans, "is close to square root of", x)


# 3.2 Finger Exercise 2
def square_root_modified(x):
    epsilon = 0.01
    num_guesses = 0
    low = min(x, 0)
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**3 - x) >= epsilon:
        print("low =", low, "high =", high, "ans =", ans)
        num_guesses += 1
        if ans**3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print("number of guesses =", num_guesses)
    print(ans, "is close to square root of", x)


# 3.2 Finger Exercise 3
# not done
def breaking_eggs(x):
    if x < 0:
        return print("Invalid input")
    breakpoint = random.randint(1, 102)
    epsilon = 1
    num_guesses = 0
    low = min(x, 0)
    high = max(102, x)
    ans = (high + low) // 2
    while abs(high - low) >= epsilon:
        print("low =", low, "high =", high, "ans =", ans)
        num_guesses += 1
        if ans < breakpoint:
            low = ans
        elif ans > breakpoint:
            high = ans
        else:
            return print(ans)
        ans = (high + low) // 2
    print("number of guesses =", num_guesses)
    print(ans, "is close to square root of", x)


# 3.1 Finger Exercise 1
def get_largest_divisor():
    x = int(input("Enter an integer greater than 2: "))
    smallest_divisor = None
    if x % 2 == 0:
        smallest_divisor = 2
    else:
        for guess in range(3, x, 2):
            if x % guess == 0:
                smallest_divisor = guess
                break
    if smallest_divisor is not None:
        return print("Largest divisor of", x, "is", x // smallest_divisor)
    else:
        return print(x, "is a prime number")


# 3.1 Finger Exercise 2
def get_roots():
    x = int(input("Enter an integer: "))
    ans = []
    root = 1
    while root <= x:
        for power in range(2, 6):
            if root ** power == x:
                ans.append([root, power])
        root += 1
    if len(ans) == 0:
        return print("Nothing found")
    else:
        for pair in ans:
            print(pair[0])
        return print("Found the following pairs:", ans)


# executions
# square_root(-25.0)
# square_root_modified(-125)
# breaking_eggs(102)
# get_largest_divisor()
get_roots()
