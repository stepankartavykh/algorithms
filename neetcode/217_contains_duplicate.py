from typing import List


def test():
    assert Solution().containsDuplicate([1,2,3,1]) == True
    assert Solution().containsDuplicate([1,2,3,4]) == False
    assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    print('all tests passed!')


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    test()
