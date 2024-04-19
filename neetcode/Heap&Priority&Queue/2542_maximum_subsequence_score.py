import heapq
import itertools


def max_score(nums1: list[int], nums2: list[int], k: int) -> int:
    res = 0
    sorted_indices = sorted(range(len(nums2)), key=lambda i: nums2[i])
    sorted_nums2 = [nums2[i] for i in sorted_indices]
    sorted_nums1 = [nums1[i] for i in sorted_indices]

    for combination in itertools.combinations(sorted_indices, k):
        min_value = sorted_nums2[min(combination)]
        max_sum_cur = 0
        for i in combination:
            max_sum_cur += sorted_nums1[i]

        res = max(res, min_value * max_sum_cur)

    return res


def max_score_second_solution(nums1: list[int], nums2: list[int], k: int) -> int:
    # TODO - resolve later!
    pairs = [elem for elem in zip(nums1, nums2)]
    pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

    min_heap = []
    num_sum = 0
    res = 0

    for sum_member, min_value in pairs:
        num_sum += sum_member
        heapq.heappush(min_heap, sum_member)
        # TODO - analysis is required!
        if len(min_heap) > k:
            num_sum -= heapq.heappop(min_heap)
        if len(min_heap) == k:
            res = max(res, num_sum * min_value)

    return res


if __name__ == '__main__':
    print(max_score_second_solution(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))
    print(max_score_second_solution(nums1=[2, 1, 14, 12], nums2=[11, 7, 13, 6], k=3))
