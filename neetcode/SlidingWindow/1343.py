from typing import List


def num_of_sub_arrays(arr: List[int], k: int, threshold: int) -> int:
    count = 0

    s = sum(arr[:k - 1])

    left = 0
    while left < len(arr) - k + 1:
        s += arr[left + k - 1]
        if s / k >= threshold:
            count += 1
        s -= arr[left]
        left += 1

    print(count)
    return count


if __name__ == '__main__':
    print(num_of_sub_arrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 2) == 3)
