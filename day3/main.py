import copy


def read_data():
    with open("input.txt") as inp:
        data_list = inp.read().splitlines()

    return data_list


def split_list(list_input):
    result = [i.strip() for i in list_input.split(',')]
    return result


def path(list1):
    x_length = 0
    y_length = 0
    coords = []
    steps = 0
    for element in list1:
        x = 0
        while x < int(element[1:]):
            if element[0] == 'R':
                x_length += 1
            elif element[0] == 'L':
                x_length += -1
            elif element[0] == 'U':
                y_length += 1
            elif element[0] == 'D':
                y_length += -1
            x += 1
            steps += 1
            current_coord = (x_length, y_length)
            coords.append(current_coord[:])

    return coords


def steps_to_intersection(list1, intersection):
    x_length = 0
    y_length = 0
    steps = 0
    for element in list1:
        x = 0
        while x < int(element[1:]):
            if element[0] == 'R':
                x_length += 1
            elif element[0] == 'L':
                x_length += -1
            elif element[0] == 'U':
                y_length += 1
            elif element[0] == 'D':
                y_length += -1
            x += 1
            steps += 1
            current_coord = (x_length, y_length)
            if current_coord == intersection:
                return steps
    return steps


def intersection(fst_path, snd_path):
    intersections = list(set(fst_path).intersection(snd_path))

    return intersections


def closest_intersection(intersections):
    closest = intersections[0][0] + intersections[0][1]
    for x in intersections:
        if abs(x[0]) + abs(x[1]) < closest:
            closest = abs(x[0]) + abs(x[1])
    return closest


def least_steps(list1, list2, intersections):
    steps = []
    for i in intersections:
        steps.append(steps_to_intersection(list1, i) + steps_to_intersection(list2, i))
    steps.sort()
    return steps[0]




data = read_data()
first_cmd = split_list(data[0])
second_cmd = split_list(data[1])
first_path = path(first_cmd)
second_path = path(second_cmd)
intersections = intersection(first_path, second_path)
print("Closest to origin:", closest_intersection(intersections))
print("Least steps:", least_steps(first_cmd, second_cmd, intersections))

