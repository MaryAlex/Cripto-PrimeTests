from fractions import gcd

from Number import Number
from TestMapping import TestMapping
from Utils import *


class PrimeTests:
    @staticmethod
    def run(n, r, test):
        if n % 2 == 0:
            return False
        a = Number(n, n - 1)
        while a > 0 and r > 0:
            if not (gcd(a, n) == 1 and PrimeTests.condition_of_test(test, a, n)):
                return False
            a -= 1
            r -= 1
        return True

    @staticmethod
    def condition_of_test(test, a, n):
        if test == TestMapping.Fermat.value:
            return PrimeTests.Fermat(a, n)
        elif test == TestMapping.MillerRabin.value:
            return PrimeTests.Miller_Rabin(n, a)
        elif test == TestMapping.SolovayStrassen.value:
            return PrimeTests.Solovay_Strassen(n, a)
        elif test == TestMapping.Exit.value:
            exit()
        else:
            print('Wrong input')
            return False

    @staticmethod
    def Fermat(a, n):
        return a ** (n - 1) == 1

    @staticmethod
    def Miller_Rabin(n, a):
        s = get_max_power_of_two_that_divide_number(n - 1)
        d = (n - 1) // (1 << s)
        return a ** d == 1 or PrimeTests._is_exist_r(a, s, d)

    @staticmethod
    def Solovay_Strassen(n, a):
        return a ** ((n - 1) // 2) == jacobi(a, n)

    @staticmethod
    def _is_exist_r(a, s, d):
        r = 0
        while r < s:
            if a ** ((1 << r) * d) == -1:
                return True
            r += 1
        return False
