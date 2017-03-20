def is_equals_in_group(number_one, number_two, group):
    return (number_one % group.n) == number_two


def is_equals_one(number, group):
    return is_equals_in_group(number, 1, group)


def is_equals_one_in_power(number, power_number, group):
    return is_equals_one(number ** power_number, group)


def is_equals_minus_one_in_power(number, power_number, group):
    return is_equals_in_power(number, power_number, group.n - 1, group)


def is_equals_in_power(number_one, power_number, number_two, group):
    return is_equals_in_group(number_one ** power_number, number_two, group)


def get_max_power_of_two_that_divide_number(number):
    tmp = number
    s = 0
    while tmp % 2 == 0:
        s += 1
        tmp /= 2
    return s
