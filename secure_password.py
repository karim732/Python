# for more secure password handling
# Normal comparing of password is vulnerable to timing attacks, compare_digest is cryptographic and not vulnerable to timing attacks

from secrets import compare_digest

my_input = 'webhub123'
password = 'webhub123'

print(compare_digest(my_input, password))