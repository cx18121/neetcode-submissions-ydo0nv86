class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findMaxFreq(d):
            ret = 0
            for k, v in d.items():
                if v > ret:
                    ret = v
            return ret

        l = 0
        r = 0
        freq = defaultdict(int)
        ret = 0
        while (r < len(s)):
            freq[s[r]] += 1
            r += 1
            while (r - l - findMaxFreq(freq) > k):
                freq[s[l]] -= 1
                l += 1
            ret = max(ret, r - l)
        return ret
            
    

        