import math, mortgage

home = float(input('Home price: '))
mindown = int(input('Minimum down payment: '))
maxdown = int(input('Maximum down payment: '))
interest = float(input('Interest rate: '))
term = float(input('Loan term (years): '))

periods = term * 12
rate = interest / 100 / 12

for down in range(mindown, maxdown, 1000):
	loan =  home - float(down)
	monthly = mortgage.mortgage_payment(loan, periods, rate)
	print(str(down) + " " + str(round(monthly,2)))