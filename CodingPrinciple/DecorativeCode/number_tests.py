from math import isqrt

class NumberTests:
    @staticmethod
    def pass_all(x):
        return True

    @staticmethod
    def is_even(x):
        return x % 2 == 0

    @staticmethod
    def is_odd(x):
        return not NumberTests.is_even(x)

    @staticmethod
    def is_prime(x):
        if x == 2:
            return True
        if x < 2 or x % 2 == 0:
            return False
        for i in range(3, isqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True

    @staticmethod
    def is_perfect_square(x):
        if x <= 1:
            return True
        lo, hi = 1, x
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_square = mid * mid
            if mid_square == x:
                return True
            elif mid_square < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    @staticmethod
    def is_fibonacci(x):
        return NumberTests.is_perfect_square(5 * x * x + 4) or NumberTests.is_perfect_square(5 * x * x - 4)

    @staticmethod
    def is_fibo_and_odd(x):
        return NumberTests.is_fibonacci(x) and NumberTests.is_odd(x)
