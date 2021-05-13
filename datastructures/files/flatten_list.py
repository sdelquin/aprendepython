input_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

output_list = []
for item in input_list:
    if type(item) == list:
        output_list.extend(item)
    else:
        output_list.append(item)

print(output_list)
