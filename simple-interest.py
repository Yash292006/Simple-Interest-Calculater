# Program to calculate simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

# Program to calculate compound interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time (in years): "))
n = int(input("Enter number of times interest applied per year: "))

# Compound Interest formula: A = P * (1 + r/n)^(n*t)
amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

print("Compound Interest:", compound_interest)
