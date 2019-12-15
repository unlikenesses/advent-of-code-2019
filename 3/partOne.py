paths = []

with open('input.txt') as input:
    for line in input:
        paths.append(line.rstrip('\n').split(','))

def parseSegment(segment):
    direction, distance = segment[:1], segment[1:]
    return {'direction': direction, 'distance': int(distance)}

def calculatePoints(path):
    oldX = 0
    oldY = 0
    points = []
    for segment in path:
        parsed = parseSegment(segment)
        if parsed['direction'] == 'R':
            newX = oldX + parsed['distance']
            for x in range(oldX, newX):
                points.append((x, oldY))
            oldX = newX
        elif parsed['direction'] == 'L':
            newX = oldX - parsed['distance']
            for x in range(oldX, newX, -1):
                points.append((x, oldY))
            oldX = newX
        elif parsed['direction'] == 'D':
            newY = oldY + parsed['distance']
            for y in range(oldY, newY):
                points.append((oldX, y))
            oldY = newY
        elif parsed['direction'] == 'U':
            newY = oldY - parsed['distance']
            for y in range(oldY, newY, -1):
                points.append((oldX, y))
            oldY = newY
    return points

def intersection(path1, path2):
    return set(path1) & set(path2)

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def calculate_distances_to_origin(points):
    distances = []
    origin = (0, 0)
    for point in points:
        distance = manhattan_distance(origin, point)
        if (distance > 0):
            distances.append(distance)
    return distances

path_1_points = calculatePoints(paths[0])
path_2_points = calculatePoints(paths[1])
intersecting_points = intersection(path_1_points, path_2_points)
distances = calculate_distances_to_origin(intersecting_points)
print(min(distances))
