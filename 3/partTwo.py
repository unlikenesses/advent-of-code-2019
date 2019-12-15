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

path_1_points = calculatePoints(paths[0])
path_2_points = calculatePoints(paths[1])
intersecting_points = set(path_1_points) & set(path_2_points)
sums = []
for intersection in intersecting_points:
    path_1_steps = path_1_points.index(intersection)
    path_2_steps = path_2_points.index(intersection)
    if (path_1_steps != 0 and path_2_steps != 0):
        sums.append(path_1_steps + path_2_steps)

print(min(sums))
