CONTROL_TABLE = 'TRWAGMYFPDXBNUZSQVHLCKE'

nif = '12345678'
control_digit = CONTROL_TABLE[int(nif) % 23]
whole_nif = nif + control_digit

print(whole_nif)
