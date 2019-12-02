
def main():
    data = read_data()
    print("Sum:", total_fuel(data))


def read_data():
    with open("input.txt") as inp:
        data = inp.read().split()
    return data


def total_fuel(data):
    total = 0
    for mass in data:
        total += required_fuel(mass)
    return total


def calc_fuel(value):
    mass = int(value)
    divide = int(mass / 3)
    fuel = divide - 2

    return fuel


def required_fuel(mass):
    calc = calc_fuel(mass)
    total = calc_fuel(mass)
    while calc >= 6:
        calc = calc_fuel(calc)
        total += calc

    return total


main()
