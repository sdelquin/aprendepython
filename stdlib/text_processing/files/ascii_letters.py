import string

text = 'This is it'

text = text.replace(' ', '')
is_ascii = [letter in string.ascii_letters for letter in text]
print(all(is_ascii))
