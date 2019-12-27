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

min_zeros = 100
min_zeros_layer = []
for layer in layers:
    num_zeros = layer.count(0)
    if num_zeros < min_zeros:
        min_zeros = num_zeros
        min_zeros_layer = layer

num_1_digits = min_zeros_layer.count(1)
num_2_digits = min_zeros_layer.count(2)
print(num_1_digits * num_2_digits)