from typing import Iterable

def sum_of_squares(nums: Iterable[int]) -> int:
    """
    Compute the sum of squares of the given integers.

    Args:
        nums: An iterable of integers.

    Returns:
        The sum of each number squared.
    """
    return sum(n * n for n in nums)

def main():
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [3, 4, 7, 8, 9]

    result1 = sum_of_squares(numbers1)
    result2 = sum_of_squares(numbers2)

    print(result1, result2)

if __name__ == "__main__":
    main()
