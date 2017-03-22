from random import random


def get_max_power_of_two_that_divide_number(number):
    tmp = number
    s = 0
    while tmp & 1 == 0:
        s += 1
        tmp >>= 1
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


def get_number(number_of_bits):
    number = '1'
    for i in range(1, number_of_bits - 1):
        number += str(round(random()))
    number += '1'
    return int(number, 2)
