def rob_bruteforce(nums: list[int]) -> int:
    # TODO Can we optimise bruteforce approach - backtracking? - Time Limit Exceeded
    max_amount = 0

    def backtrack(i, current):
        nonlocal max_amount
        if i >= len(nums):
            max_amount = max(max_amount, sum(current))
            return

        current.append(nums[i])
        backtrack(i + 2, current)
        current.pop()
        backtrack(i + 1, current)

    backtrack(0, [])
    backtrack(1, [])

    return max_amount


def test_approach(nums: list[int]) -> int:
    # TODO: test approach
    def help_func(houses, i):
        if i < 0:
            return 0
        return max(help_func(nums, i - 2) + houses[i], help_func(houses, i - 1))

    return help_func(nums, len(nums) - 1)


def rob_solution(nums: list[int]) -> int:
    # TODO: resolve is required!
    rob_first_position, rob_second_position = 0, 0

    for n in nums:
        next_robbery_amount = max(n + rob_first_position, rob_second_position)
        rob_first_position = rob_second_position
        rob_second_position = next_robbery_amount

    return rob_second_position


if __name__ == '__main__':
    print(rob_solution([1, 2, 3, 1]))
    print(rob_solution([2, 7, 9, 3, 1]))
    print(rob_solution([6, 2, 1, 6]))
    print(rob_solution([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
                        168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]))
