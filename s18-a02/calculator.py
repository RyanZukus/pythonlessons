import math, mortgage

home = float(input('Home price: '))
down = float(input('Down payment: '))
interest = float(input('Interest rate: '))
term = float(input('Loan term (years): '))

loan =  home - down
periods = term * 12
rate = interest / 100 / 12

monthly = mortgage.mortgage_payment(loan, periods, rate)

print("\nMonthly payment: " + str(round(monthly,2)))