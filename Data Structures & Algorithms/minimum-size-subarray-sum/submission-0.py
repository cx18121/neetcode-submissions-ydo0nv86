class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        psum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= target:
                return 1
            psum[i] = nums[i-1] + psum[i-1]
        ret = float('inf')
        for i in range(0, len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                if psum[j] - psum[i] >= target:
                    ret = min(j - i, ret)
                    break
        if ret == float('inf'):
            return 0
        return ret