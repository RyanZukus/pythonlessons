# Q5: How many detectives?
import helper

data = helper.read_salaries()
jobs = helper.get_column(data, 2)
print(helper.count(jobs, 'DETECTIVE'))