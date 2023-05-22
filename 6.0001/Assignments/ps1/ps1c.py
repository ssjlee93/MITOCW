# Part C
# problem assumes user will enter valid input. try-catch not required
# find the % of monthly salary to save given # of months and salary
annual_salary = float(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 1.07
portion_down_payment = 0.25 * total_cost
r = 0.04
months = 36


def calculate_portion_saved(salary):
    # problem assumes approximation algorithm
    # use bisection search
    epsilon = 100
    num_guesses, low = 0, 0
    high = 10000
    ans = (high + low) // 2
    # checking for impossibility
    if calculate_savings(annual_salary, high) < portion_down_payment:
        return print("It is not possible to pay the down payment in three years.")
    current_savings = calculate_savings(annual_salary, ans)
    while abs((portion_down_payment - current_savings)) >= epsilon:
        # finish the loop if the algorithm repeats itself
        if ans == high or ans == low:
            break
        print("low:", low, "high:", high, "ans:", ans)
        num_guesses += 1
        current_savings = calculate_savings(annual_salary, ans)
        print("  current_savings:", current_savings)
        if current_savings > portion_down_payment:
            high = ans
        else:
            low = ans
        ans = (high + low) // 2
    print("Best savings rate:", ans / 10000)
    print("Steps in bisection search:", num_guesses)
    return


def calculate_savings(salary, portion_saved) -> int:
    savings = 0
    for i in range(36):
        investment = savings * (0.04 / 12)
        monthly_saving = (salary / 12) * (portion_saved / 10000)
        savings = savings + investment + monthly_saving
        if i % 6 == 0:
            salary = salary * 1.07
    return round(savings, 2)


calculate_portion_saved(annual_salary)


# integer division in python : `//`
#   better than type casting to int()
#   better than rounding to 0 decimal places
# logical operators : `and` `or`
# my algorithms is inspired by the code in the book
