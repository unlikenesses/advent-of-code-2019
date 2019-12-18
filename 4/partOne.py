min = 138307
max = 654504

def valid(password):
    if len(password) != 6:
        return False
    has_double = False
    old_digit = 0
    for digit in password:
        if int(digit) < old_digit:
            return False
        if int(digit) == old_digit:
            has_double = True
        old_digit = int(digit)
    return has_double

num_passwords = 0
for n in range(min, max):
    if valid(str(n)):
        num_passwords += 1

print(num_passwords)

