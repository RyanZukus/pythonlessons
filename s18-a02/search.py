import math, mortgage

home = float(input('Home price: '))
interest = float(input('Interest rate: '))
term = float(input('Loan term (years): '))
monthlygoal = float(input('Desired monthly payment: '))

loanhi =  home
loanlo = 0

periods = term * 12
rate = interest / 100 / 12

while True:
	loan = (loanlo + loanhi) / 2
	floan = mortgage.mortgage_payment(loan, periods, rate) - monthlygoal
	if abs(floan) < 0.01:
		break
	elif floan < 0:
		loanlo = loan
	else:
		loanhi = loan

down = home - loan

print("\nDown payment: " + str(round(down,2)))