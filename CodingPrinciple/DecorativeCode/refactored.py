from typing import List
from number_tests import NumberTests

class Refactored:
    @staticmethod
    def sum_by_test(nums: List[int], selector):
        sum = 0
        for num in nums:
            if selector(num):
                sum += num
        return sum

    @staticmethod
    def sum_by_test_refactored(nums: List[int], selector):
        nums = filter(selector, nums)
        s = sum(filter(selector, nums))
        return s



if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    print(Refactored.sum_by_test_refactored(nums, NumberTests.pass_all))
    print(Refactored.sum_by_test_refactored(nums, lambda x: True))

    print(Refactored.sum_by_test_refactored(nums, NumberTests.is_even))
    print(Refactored.sum_by_test_refactored(nums, lambda x: x % 2 == 0))

    print(Refactored.sum_by_test_refactored(nums, NumberTests.is_odd))
    print(Refactored.sum_by_test_refactored(nums, lambda x: x % 2 != 0))

    print(Refactored.sum_by_test_refactored([1,2,3,4,5,6,7,8,9,10,11,12,13,1,4,15], NumberTests.is_prime))

    print(Refactored.sum_by_test_refactored([1,2,3,4,5,6,7,8,9,10,11,12,13,1,4,15], NumberTests.is_fibonacci))
