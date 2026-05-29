class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * (n + 1)
        suf = [1] * (n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1] * nums[i-1]
            suf[n-i] = suf[n - i + 1] * nums[n - i]        
        
        output = []
        for i in range(0,n):
            output.append(pref[i] * suf[i+1])
        print(pref)
        print(suf)
        return output