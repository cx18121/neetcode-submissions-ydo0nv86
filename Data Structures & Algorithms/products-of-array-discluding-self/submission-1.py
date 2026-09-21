class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * (n + 1)
        suf = [1] * (n + 1)

        for i in range(1, n+1):
            pre[i] = pre[i-1] * nums[i-1]
            suf[n-i] = suf[n+1-i] * nums[n-i]


        out = []
        for i in range(n):
            out.append(pre[i] * suf[i+1])
        return out
    