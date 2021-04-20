def get_int():
    while True:
        user_input = input('Give me an integer number: ')
        try:
            value = int(user_input)
        except ValueError:
            print('Not a valid integer. Try it again!')
        else:
            return value


get_int()
