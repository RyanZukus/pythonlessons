# Q4: How many employees in the police department?
import helper

data = helper.read_salaries()
department = helper.get_column(data, 3)
print(helper.count(department, 'POLICE'))