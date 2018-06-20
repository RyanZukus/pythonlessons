# Q8: What are the minimum, mean, median, and maximum salaries?
import helper

data = helper.read_salaries()

rawsalaries = helper.get_column(data,-2)
salaries = []

for entry in rawsalaries:
	if len(entry) > 0:
		salaries.append(float(entry))

print('Minimum:', min(salaries))
print('Mean:', helper.mean(salaries))
print('Median:', helper.median(salaries))
print('Maximum:', max(salaries))
