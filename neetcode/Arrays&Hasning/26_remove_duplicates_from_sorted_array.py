def remove_duplicates(nums: list[int]) -> int:
    # TODO there is a better way. Make a replacement instead of deleting.
    visited_numbers = set()
    index = 0
    length = len(nums)
    while index < length:
        if nums[index] not in visited_numbers:
            visited_numbers.add(nums[index])
        else:
            del nums[index]
            index -= 1
            length -= 1

        index += 1

    return len(visited_numbers)


if __name__ == '__main__':
    numbers = [1, 1, 2]
    print(remove_duplicates(numbers), numbers)
    numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(numbers), numbers)
