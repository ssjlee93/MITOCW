# Part B
# problem assumes user will enter valid input. try-catch not required
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

# find # of months for portion_down_payment with increasing salary every 6 months
month = 0
while current_savings < portion_down_payment:
    investment = current_savings * (r / 12)
    monthly_saving = (annual_salary / 12) * portion_saved
    current_savings = current_savings + investment + monthly_saving
    month += 1
    if month % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
print("Number of months:", month)

