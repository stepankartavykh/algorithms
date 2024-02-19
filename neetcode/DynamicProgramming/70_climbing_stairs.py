def climb_stairs(n: int) -> int:
    counter = 0

    def bruteforce(current_sum):
        nonlocal counter

        if current_sum > n:
            return

        result_one = current_sum + 1
        result_second = current_sum + 2

        counter += (result_one == n) + (result_second == n)

        bruteforce(result_one)
        bruteforce(result_second)

    bruteforce(0)

    return counter


def dp_algo(n: int) -> int:
    # TODO make analysis and resolve again!
    one, two = 1, 1

    for _ in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


if __name__ == '__main__':
    print(dp_algo(n=1))
    print(dp_algo(n=2))
    print(dp_algo(n=3))
    print(dp_algo(n=4))
    print(dp_algo(n=5))
