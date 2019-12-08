import math;

sum = 0

def calculate_fuel(mass):
    return (int(mass) // 3) - 2

with open('input.txt') as input:
    for line in input:
        module_fuel = calculate_fuel(line)
        fuel_fuel = calculate_fuel(module_fuel)
        while fuel_fuel > 0:
            module_fuel += fuel_fuel
            fuel_fuel = calculate_fuel(fuel_fuel)
        sum += module_fuel

print(sum)