# 1. How many employees does the city have?
# Hint: wc
grep \\$ salaries.csv | wc -l

# 2. How many full-time workers are there in the file?
# Hint: grep for ',F,' then use wc
grep ,F, salaries.csv | wc -l

# 3. How many part-time workers are there in the file?
grep ,P, salaries.csv | wc -l

# 4. How many people work for the police department?
# Hint: grep for POLICE then use wc
grep POLICE salaries.csv | wc -l

# 5. How many of them are detectives?
# Hint: grep for POLICE then grep for DETECTIVE then use wc
grep POLICE salaries.csv | grep DETECTIVE | wc -l

# 6. Which department has the most employees?
# Hint: see Scripts section of Command Line slides
cut -d, -f4 salaries.csv | sort | uniq -c | sort -n | tail -1