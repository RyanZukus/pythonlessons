# A.1: Parse the included salaries.csv file.
# Your parser should split each line on ',' and return a nested list 
# where each element is itself a list of fields. 
# Additionally you should ignore/remove the first (header) line.
def read_salaries():
	file = open('salaries.csv')
	salaries = []
	for line in file:
		fields = line[:-1].split(',')
		salary = fields[-2]
		hourly = fields[-1]

		if len(salary) > 0 and salary[0] == "$":
			fields[-2] = float(salary[1:])
		if len(hourly) > 0 and hourly[0] == "$":
			fields[-1] = float(hourly[1:])

		salaries.append(fields)

	salaries.pop(0)
	return(salaries)

# A.2: Given a 2d list data and an integer column_index 
# return a 1d list of values for that column.
def get_column(data, column_index):
	column = []
	for row in data:
		column.append(row[column_index])
	return column

# A.3: Given a 1d list of `values` (e.g. the result of get_column), 
# return the number of elements that are equal to `search_value`.
def count(values, search_value):
	count = 0
	for value in values:
		if value == search_value:
			count += 1
	return count

# A.4: Given a 1d list values (e.g. the result of get_column),
# return a dictionary of value-count pairs.
def counts(values):
	counts = dict()
	for value in values:
		if value in counts:
			counts[value] += 1
		else:
			counts[value] = 1
	return counts

# A.5: Given a dictionary d with numeric values, return a list [key, value] of two elements,
# where key is the the key in d with the largest value, and value is it's value. 
def dict_max_value(d):
	mode = max(d.values())
	for entry in d:
		if d[entry] == mode:
			return [entry, mode]

# A.6: Given a list of numbers use the built-in functions sum and len to return their mean.
def mean(numbers):
	return sum(numbers)/len(numbers)

# A.7: Given a list of numbers calculate the median.
def median(numbers):
	ordered = sorted(numbers)
	length = len(ordered)
	if length % 2 > 0: # if odd
		return float(ordered[int(length / 2)])
	else: # if even
		k = int(length / 2)
		return float((ordered[k-1] + ordered[k])/2)
