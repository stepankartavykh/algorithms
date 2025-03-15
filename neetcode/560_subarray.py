class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        l, r = 0, 0
        cur_sum = 0

        while r < len(nums) and l <= r:
            cur_sum += nums[r]

            if cur_sum == k:
                res += 1
                cur_sum -= nums[l]
                l += 1
                r += 1
            elif cur_sum < k:
                r += 1
            else:
                cur_sum -= nums[l]
                l += 1
        
        return res


if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], 2))
    print(Solution().subarraySum([1, 2, 3], 3))