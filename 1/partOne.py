sum = 0

def calculate_fuel(mass):
    return (int(mass) // 3) - 2

with open('input.txt') as input:
    for line in input:
        sum += calculate_fuel(line)

print(sum)