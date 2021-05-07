word = 'ordenador'

word_length = len(word)

num_a = word.count('a')
num_e = word.count('e')
num_i = word.count('i')
num_o = word.count('o')
num_u = word.count('u')

metric = word_length * (num_a + num_e + num_i + num_o + num_u)
print(metric)
