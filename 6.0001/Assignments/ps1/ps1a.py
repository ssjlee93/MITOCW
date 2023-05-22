# Part A
# problem assumes user will enter valid input. try-catch not required
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter cost of your dream home: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
monthly_saving = (annual_salary / 12) * portion_saved
# find # of months for portion_down_payment
# portion_down_payment = x(current_savings + investments + monthly_salary*portion_saved)
month = 0
while current_savings < portion_down_payment:
    investment = current_savings * (r / 12)
    current_savings = current_savings + investment + monthly_saving
    month += 1
print("Number of months:", month)
