class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, m = 0, len(nums) - 1, (len(nums) - 1)//2

        while(True):
            print(l , m, r)
            if m == l:
                return min(nums[r], nums[m])
            elif nums[l] < nums[m] and nums[m] > nums[r]:
                l = m
                m = (r-l)//2 + l
            else:
                r = m
                m = (r-l)//2 + l
            