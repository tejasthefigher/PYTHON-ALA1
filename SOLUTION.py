print("Multi-Year Tax Simulation")
years = int(input("Enter years: "))
income = int(input("Enter initial income: "))
i = 1
total_tax = 0

while i <= years:
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = income * 5 / 100
    elif income <= 1000000:
        tax = income * 20 / 100
    else:
        tax = income * 30 / 100

    total_tax = total_tax + tax
    print("Year", i, "Tax:", tax)

    income = income + income * 10 / 100

    if tax > 100000:
        print("High tax year")
    else:
        print("Normal tax year")

    i = i + 1

print("Total tax paid:", total_tax)

if total_tax > 500000:
    print("Heavy taxpayer")
else:
    print("Moderate taxpayer")
