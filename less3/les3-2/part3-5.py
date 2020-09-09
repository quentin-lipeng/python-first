s = 'hello Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print('hello\tpython')

n = '10a-'
print(n.isalnum())
print('hello'.isalpha())
print('123'.isdigit())

print('HELLO'.isupper())
print('hello'.islower())
print('    '.isspace())

print('hello python'.startswith('he'))
print('hello python'.endswith('he'))
print('hello python'.endswith('he', 0, 5))

print('hello python'.split('o'))
