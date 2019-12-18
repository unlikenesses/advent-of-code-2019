min = 138307
max = 654504

def valid(password):
    if len(password) != 6:
        return False
    has_double = False
    old_digit = 0
    doubled_digit = None
    for digit in password:
        if int(digit) < old_digit:
            return False
        if int(digit) == old_digit:
            if has_double == False and doubled_digit != digit:
                has_double = True
                doubled_digit = digit
            elif doubled_digit == digit:
                has_double = False
        old_digit = int(digit)
    return has_double

num_passwords = 0
valid_passwords = []
for n in range(min, max):
    if valid(str(n)):
        valid_passwords.append(n)
        num_passwords += 1

print(num_passwords)
