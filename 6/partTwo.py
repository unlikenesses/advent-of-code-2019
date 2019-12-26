input_data = []
with open('input.txt') as input:
    for line in input:
        input_data.append(line.rstrip('\n'))

tree = {}

def make_tree(input_data):
    for orbit in input_data:
        parent, child = orbit.split(')')
        if (child not in tree):
            tree[child] = None
        tree[child] = parent

def recur(node, count = 0):
    while node != 'COM':
        return recur(tree[node], count + 1)
    return count + 1

def count_tree():
    count = 0
    for planet in tree:
        parent = tree[planet]
        planet_count = recur(parent)
        count += planet_count
    return count

make_tree(input_data)

def get_path_to_com(node):
    path_to_com = []
    parent = tree[node]
    while parent != 'COM':
        path_to_com.append(parent)
        parent = tree[parent]
    return path_to_com

you_to_com = get_path_to_com('YOU')
san_to_com = get_path_to_com('SAN')
# Solution to find intersection while maintaining order:
# https://stackoverflow.com/a/23529016
san_to_com_set = set(san_to_com)
intersect = [x for x in you_to_com if x in san_to_com_set]

first_planet = intersect[0]
you_to_first_planet = you_to_com.index(first_planet)
san_to_first_planet = san_to_com.index(first_planet)
print(you_to_first_planet + san_to_first_planet)