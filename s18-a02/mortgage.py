def mortgage_payment(loan, periods, rate):
	return (rate * loan) / (1 - (1+rate)**(-periods))