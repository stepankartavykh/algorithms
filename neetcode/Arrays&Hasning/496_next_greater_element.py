from typing import List


def next_greater_element_dumb_solution(nums1: List[int], nums2: List[int]) -> List[int]:
    answer = []
    for num1 in nums1:
        index2 = 0
        while nums2[index2] != num1:
            index2 += 1
            if index2 == len(nums2):
                answer.append(-1)
                break
        if index2 + 1 == len(nums2):
            answer.append(-1)
            continue
        next_greater = None
        for num2 in nums2[index2 + 1:]:
            if num2 > num1:
                next_greater = num2
                break
        if next_greater:
            answer.append(next_greater)
        else:
            answer.append(-1)
    return answer


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    result = [-1] * len(nums1)
    d1 = {
        num1: index
        for index, num1 in enumerate(nums1)
    }

    for i in range(len(nums2)):
        if nums2[i] not in d1:
            continue
        for j in range(i + 1, len(nums2)):
            if nums2[j] > nums2[i]:
                result[d1[nums2[i]]] = nums2[j]
                break
    return result


if __name__ == '__main__':
    inputs = [
        ([4, 1, 2], [1, 3, 4, 2]),
        # ([2, 4], [1, 2, 3, 4]),
    ]
    for input_ in inputs:
        print(next_greater_element(input_[0], input_[1]))
