def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    first, second, third = 0, 1, 1
    for i in range(2, n):
        temp = first + second + third
        first = second
        second = third
        third = temp

    return third


if __name__ == '__main__':
    print(tribonacci(0))
    print(tribonacci(1))
    print(tribonacci(2))
    print(tribonacci(3))
    print(tribonacci(4))
    print(tribonacci(5))
    print(tribonacci(6))
