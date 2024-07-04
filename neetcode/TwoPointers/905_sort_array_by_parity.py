from tests.TestClient import TestClient, SpecificInterface


def sort_array_by_parity(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda element: element % 2 != 0)


def sort_array_by_parity_second_solution(nums: list[int]) -> list[int]:
    even, odd = [], []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd


if __name__ == '__main__':
    test_client = TestClient([sort_array_by_parity, sort_array_by_parity_second_solution], SpecificInterface(list[int]))
    test_client.run()
