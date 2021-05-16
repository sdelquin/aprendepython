input_date = '12/31/20'

splitted_date = input_date.split('/')
day = splitted_date[1]
month = splitted_date[0]
year = '20' + splitted_date[2]

output_date = '-'.join([day, month, year])
print(output_date)
