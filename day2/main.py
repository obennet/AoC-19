import random

def main():
    data = read_data()
    print(data)
    print(run_intcode(data))
    brute_force(data, 19690720)


def brute_force(data, value_to_find):
    while data[0] != value_to_find:
        data = read_data()
        noun = random.randint(0, 99)
        verb = random.randint(0, 99)
        data[1] = noun
        data[2] = verb
        run_intcode(data)

    answer = 100*noun+verb

    print("Noun:", noun)
    print("Verb:", verb)
    print("Answer:", answer)



def read_data():
    with open("input.txt") as inp:
        data = inp.read().split(',')
    return data


def run_intcode(data):
    index = 0
    while index < len(data) - 1:
        if data[index] == '1' or '2':
            data = interpreter(data, index)
            index += 3
        elif data[index] == '99':
            break

        index += 1
    return data


def interpreter(data, index):
    first_value = int(data[index + 1])
    second_value = int(data[index + 2])
    third_value = int(data[index + 3])

    if data[index] == '1':
        data = code_one(data, first_value, second_value, third_value)

    elif data[index] == '2':
        data = code_two(data, first_value, second_value, third_value)

    return data


def code_one(data, first_value, second_value, third_value):
    amount = int(data[first_value]) + int(data[second_value])
    data[third_value] = amount
    return data


def code_two(data, first_value, second_value, third_value):
    product = int(data[first_value]) * int(data[second_value])
    data[third_value] = product
    return data


main()
