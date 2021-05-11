text = 'hello-world'

for char in text:
    if not char.isalpha():
        print('Non-alphabetic char found!')
        break
else:
    print('All chars are alphabetic')
