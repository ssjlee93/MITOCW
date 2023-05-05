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
    bpoint = 0
    print("bpoint", bpoint)
    epsilon = 0.01
    num_guesses = 0
    low = min(x, 0)
    high = max(1, x)
    ans = (high + low) / 2
    while abs(high - low) >= epsilon:
        print("low =", low, "high =", high, "ans =", ans)
        num_guesses += 1
        if ans < bpoint:
            low = ans
        elif ans > bpoint:
            high = ans
        else:
            return print(ans)
        ans = (high + low) / 2
    print("number of guesses =", num_guesses)
    print(ans, "is close to square root of", x)


# executions
# square_root(-25.0)
# square_root_modified(-125)
breaking_eggs(102)

