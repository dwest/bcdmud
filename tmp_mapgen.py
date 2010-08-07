import random

empty_char = 0
floor_char = 1
minmax_size = (3, 6)
minmax_rooms = (6, 9)
map_size = (20, 40)
upper_move = 6
num_halls = 6
density_radius = 3
max_density = 3
minmax_connect = (1, 3)

#def make_line(point1, point2, level_map):
#    if(point1[0] < 0 || point1[0] >= len(level_map) ||
#       point1[1] < 0 || point1[1] >= len(level_map) ||
#       point2[0] < 0 || point2[0] >= len(level_map) ||
#       point2[1] < 0 || point2[1] >= len(level_map)):
#        return -1   # change when find out how to do excpetions
#                    # or just catch and throw excection later on
#    while(point1 != point2):
#        diff_y = point2[0] - point1[0]
#        diff_x = point2[1] - point1[1]
#        if(diff_x < 0):
#            tmp_point = point2
#            point2 = point1
#            point1 = tmp_point
#            diff_x *= -1

#        ratio = (diff_y * 1.0) / diff_x if diff_x else diff_y

#        # change to not use magic numbers
#        # also test different ratios for better lines
#        if(ratio <= -3.5):
#            level_map[point1[0]][point1[1]] = '|'
#            point1[0] += -1
#        elif(ratio >= 3.5):
#            level_map[point1[0]][point1[1]] = '|'
#            point1[0] += 1
#        elif(-.2857 <= ratio <= .2857):
#            level_map[point1[0]][point1[1]] = '-'
#            point1[1] += 1
#        elif(ratio > 0):
#            level_map[point1[0]][point1[1]] = '\\'
#            point1[0] += 1
#            point1[1] += 1
#        else:
#            level_map[point1[0]][point1[1]] = '/'
#            point1[0] += -1
#            point1[1] += 1

def make_room(level_map, path_map):
    size = (random.randint(*minmax_size), random.randint(*minmax_size))
    coord = (random.randint(1, (map_size[0] - 2) - size[0]), random.randint(1, (map_size[1] - 2) - size[1]))
    while(not (minmax_connect[0] <= connected_noroom(coord, size, level_map, path_map) <= minmax_connect[1])):
        size = (random.randint(*minmax_size), random.randint(*minmax_size))
        coord = (random.randint(1, (map_size[0] - 2) - size[0]), random.randint(1, (map_size[1] - 2) - size[1]))
#    while(not check_placement(coord, size, level_map)):
#        size = (random.randint(*minmax_size), random.randint(*minmax_size))
#        coord = (random.randint(0,(map_size[0] - 1) - size[0]), random.randint(0,(map_size[1] - 1) - size[1]))
#        print coord, size

    for y in range(coord[0], coord[0] + size[0]):
        for x in range(coord[1], coord[1] + size[1]):
            level_map[y][x] = floor_char
    return (coord, size)

def connected_noroom(coord, size, level_map, path_map):
    connected = 0
    for y in range(coord[0], coord[0] + size[0]):
        for x in range(coord[1], coord[1] + size[1]):
            if(level_map[y][x] == floor_char):
                return 0
            if(path_map[y][x] == floor_char):
                connected += 1
    return connected

#def check_placement(coord, size, level_map):
#    x, y = coord
#    x_size, y_size = size
#    return ((y + y_size < map_size[0] - 1) and (x + x_size < map_size[1] - 1)) #and
#            (level_map[y][x] == empty_char) and
#            (level_map[y][x + x_size] == empty_char) and
#            (level_map[y + y_size][x] == empty_char) and
#            (level_map[y + y_size][x + x_size] == empty_char))

def make_halls(level_map):
    halls = num_halls
    branches = []
    while(halls):
        if(branches):
            point1 = branches[random.randint(0, len(branches) - 1)]
        else:
            point1 = [random.randint(1, map_size[0] - 2), random.randint(1, map_size[1] - 2)]
        
        point2 = [random.randint(1, map_size[0] - 2), random.randint(1, map_size[1] - 2)]
        while(check_density(point2, level_map, density_radius) > max_density):
            point2 = [random.randint(1, map_size[0] - 2), random.randint(1, map_size[1] - 2)]
        branches = []

        while(point1 != point2):
            point1 = make_path(point1, point2, level_map)
            branches.append(point1)

        halls -= 1

def check_density(point, level_map, radius):
    dens = 0
    if(point[0] - radius < 0):
        radius = point[0]
    elif(point[0] + radius >= map_size[0]):
        radius = (map_size[0] - 1) - point[0]
    if(point[1] - radius < 0):
        radius = point[1]
    elif(point[1] + radius >= map_size[1]):
        radius = (map_size[1] - 1) - point[1]

    for row in level_map[point[0] - radius:point[0] + radius + 1]:
        for col in row[point[1] - radius:point[1] + radius + 1]:
#    for y in range(point[0] - radius, point[0] + radius):
#        for x in range(point[1] - radius, point[1] + radius):
#            if(level_map[y][x] == floor_char):
            if(col == floor_char):
                dens += 1
    return dens

def make_path(point1, point2, level_map):
    diff = [0, 0]
    diff[0] = point2[0] - point1[0]
    diff[1] = point2[1] - point1[1]

    if(diff[0] == 0):
        direct = 1
        neg = 1 if diff[1] > 0 else -1
        move = random.randint(1, upper_move)
    elif(diff[1] == 0):
        direct = 0
        neg = 1 if diff[0] > 0 else -1
        move = random.randint(1, upper_move)
    else:
        randtest = random.randint(0,1)
        direct = randtest
        neg = 1 if diff[randtest] > 0 else -1
        move = random.randint(1, upper_move)

    bound = point1[direct] + (neg * move)
    if(bound < 1):
        move = move + bound - 1
    elif(bound > map_size[direct] - 2):
        move = map_size[direct] - point1[direct] - 2

    while(move):
        level_map[point1[0]][point1[1]] = floor_char
        point1[direct] += neg
        move -= 1

    return point1

def make_level():
    level_map = [map_size[1] * [empty_char] for count in range(0, map_size[0])]
    path_map = [map_size[1] * [empty_char] for count in range(0, map_size[0])]
    make_halls(path_map)
    num_rooms = random.randint(*minmax_rooms)
    num_rooms = minmax_rooms[1]
    while(num_rooms):
        room = make_room(level_map, path_map)
        num_rooms = num_rooms - 1
    
    for y in range(0, map_size[0]):
        for x in range(0, map_size[1]):
            if(path_map[y][x] == floor_char):
                level_map[y][x] = floor_char

    return level_map
#    print_map(path_map)
#    print_map(level_map)

def print_map(level_map):
    for row in level_map:
        for col in row:
            print col,
        print
    print

make_level()
