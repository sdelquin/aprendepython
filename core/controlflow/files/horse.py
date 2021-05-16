TARGET_X = 7
TARGET_Y = 8

horse_x = 0
horse_y = 0
print(f'({horse_x}, {horse_y})', end=' ')

flow = True
while horse_x != TARGET_X and horse_y != TARGET_Y:
    if flow:
        horse_x += 1
        horse_y += 2
    else:
        horse_x += 2
        horse_y += 1
    print(f'({horse_x}, {horse_y})', end=' ')
    flow = not flow
