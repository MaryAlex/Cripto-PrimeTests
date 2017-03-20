from fractions import gcd

from Group import Group
from Utils import *


class PrimeTests:
    @staticmethod
    def Fermat(n, r):
        a = n - 1
        while a > 0 and r > 0:
            if gcd(a, n) == 1:
                if not is_equals_one_in_power(a, n - 1, Group(n)):
                    return False
            a -= 1
            r -= 1
        return True

    @staticmethod
    def Miller_Rabin(n, r):
        a = n - 1
        s = get_max_power_of_two_that_divide_number(n - 1)
        d = (n - 1) / (2 ** s)
        while a > 0 and r > 0:
            if not (is_equals_one_in_power(a, d, Group(n)) or PrimeTests._is_exist_r(a, s, d, n)):
                return False
            a -= 1
            r -= 1
        return True

    @staticmethod
    def Solovay_Strassen(n, r):
        if n % 2 == 0:
            print('Even number on Solovay-Strassen test')
            return False
        a = n - 1
        while a > 0 and r > 0:
            if gcd(a, n) > 1:
                return False
            if not is_equals_in_power(a, (n-1)/2, a/n, Group(n)):
                return False
            a -= 1
            r -= 1
        return True

    @staticmethod
    def _is_exist_r(a, s, d, n):
        r = 0
        while r < s:
            if is_equals_minus_one_in_power(a, (2 ** r) * d, Group(n)):
                return True
            r += 1
        return False
