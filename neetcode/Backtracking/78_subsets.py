from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]

    def find_solutions(input_nums):
        if input_nums not in result:
            result.append(input_nums)
        else:
            return

        for i in range(len(input_nums)):
            for j in range(i, len(input_nums)):
                find_solutions(nums[i:j])

    find_solutions(nums)

    return result


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
