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
print(count_tree())