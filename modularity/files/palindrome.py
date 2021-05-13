def is_palindrome(word):
    word = word.replace(' ', '')
    return word == word[::-1]


print(is_palindrome('ana lava lana'))
