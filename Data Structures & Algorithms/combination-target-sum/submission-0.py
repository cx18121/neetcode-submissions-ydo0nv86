class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, lst, cur):
            if cur == target:
                res.append(lst[:])
                return
            if i >= len(nums) or cur > target:
                return
            lst.append(nums[i])
            dfs(i, lst, cur + nums[i])
            lst.pop()
            dfs(i + 1, lst, cur)
        
        dfs(0,[], 0)
        return res
