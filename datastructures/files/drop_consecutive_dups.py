input_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

output_list = []
previous_item = None
for current_item in input_list:
    if current_item != previous_item:
        output_list.append(current_item)
        previous_item = current_item

print(output_list)
