from random import random


def is_modulo_equals(number_one, number_two, modulo):
    return number_one == (number_two if number_two > 0 else modulo + number_two)


def is_equals_one(number, modulo):
    return is_modulo_equals(number, 1, modulo)


def is_equals_one_in_power(number, power_number, modulo):
    return is_equals_one(pow(number, power_number, modulo), modulo)


def is_equals_minus_one_in_power(number, power_number, modulo):
    return is_equals_in_power(number, power_number, modulo - 1, modulo)


def is_equals_in_power(number_one, power_number, number_two, modulo):
    return is_modulo_equals(pow(number_one, power_number, modulo), number_two, modulo)


def get_max_power_of_two_that_divide_number(number):
    tmp = number
    s = 0
    while tmp % 2 == 0:
        s += 1
        tmp //= 2
    return s


def jacobi(a, n):
    s = 1
    while True:
        if n < 1: raise ValueError("Too small module for Jacobi symbol: " + str(n))
        if n & 1 == 0: raise ValueError("Jacobi is defined only for odd modules")
        if n == 1: return s
        a = a % n
        if a == 0: return 0
        if a == 1: return s

        if a & 1 == 0:
            if n % 8 in (3, 5):
                s = -s
            a >>= 1
            continue

        if a % 4 == 3 and n % 4 == 3:
            s = -s

        a, n = n, a
    return


def get_number(l):
    number = '1'
    for i in range(1, l-1):
        number += str(round(random()))
    number += '1'
    return int(number, 2)
