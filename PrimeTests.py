from fractions import gcd

from TestMapping import TestMapping
from Utils import *


class PrimeTests:
    @staticmethod
    def run(n, r, test):
        a = n - 1
        while a > 0 and r > 0:
            if not PrimeTests.condition_of_test(test, n, a):
                return False
            a -= 1
            r -= 1
        return True

    @staticmethod
    def condition_of_test(test, n, a):
        if n % 2 == 0:
            return False
        if test == TestMapping.Fermat.value:
            return PrimeTests.Fermat(n, a)
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
    def Fermat(n, a):
        return gcd(a, n) == 1 and is_equals_one_in_power(a, n - 1, n)

    @staticmethod
    def Miller_Rabin(n, a):
        s = get_max_power_of_two_that_divide_number(n - 1)
        d = (n - 1) // (2 ** s)
        return is_equals_one_in_power(a, d, n) or PrimeTests._is_exist_r(a, s, d, n)

    @staticmethod
    def Solovay_Strassen(n, a):
        return not gcd(a, n) > 1 and is_equals_in_power(a, (n - 1) // 2, jacobi(a, n), n)

    @staticmethod
    def _is_exist_r(a, s, d, n):
        r = 0
        while r < s:
            if is_equals_minus_one_in_power(a, pow(2, r) * d, n):
                return True
            r += 1
        return False
