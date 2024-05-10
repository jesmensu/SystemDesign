from typing import List

class BadCode:
    @staticmethod
    def sum_all(nums: List[int]) -> int:
        sum = 0
        for num in nums:
                sum += num
        return sum

    @staticmethod
    def sum_all_odd(nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if num % 2 != 0:
                sum += num
        return sum

    @staticmethod
    def sum_all_even(nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if num % 2 == 0:
                sum += num
        return sum

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(BadCode.sum_all(nums))
    print(BadCode.sum_all_odd(nums))
    print(BadCode.sum_all_even(nums))
