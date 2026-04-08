class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ret = float('inf')
        tot = 0

        for i in range(len(nums)):
            tot += nums[i]
            while tot >= target:
                ret = min(i - l + 1, ret)
                tot -= nums[l]
                l += 1
            
        if ret == float('inf'):
            return 0
        else: return ret
            
        


        
