# Q2: How many full time employees are there?
import helper

data = helper.read_salaries()
timing = helper.get_column(data, 4)
print(helper.count(timing, 'F'))