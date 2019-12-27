with open('input.txt', 'r') as f:
    input_data = [int(x) for x in f.read().strip('\n')]

def chunk(layers, n):
    for i in range(0, len(layers), n):
        yield layers[i:i + n]

width = 25
height = 6
pixels_per_layer = width * height
num_layers = len(input_data) / pixels_per_layer

layers = list(chunk(input_data, pixels_per_layer))

def get_pos(x, y):
    return (y * width) + x

def calculate_pixel(x, y):
    for layer in layers:
        layer_pixel = layer[get_pos(x, y)]
        if layer_pixel == 0:
            return ' '
        if layer_pixel == 1:
            return '*'

for y in range(0, height):
    for x in range(0, width):
        print(calculate_pixel(x, y), end='')
    print()