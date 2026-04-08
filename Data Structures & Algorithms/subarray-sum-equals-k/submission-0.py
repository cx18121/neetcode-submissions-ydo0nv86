class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = 0
        psum = 0
        hmap = defaultdict(int)
        hmap[0] = 1
        for i, n in enumerate(nums):
            psum += n
            if psum - k in hmap:
                ct += hmap[psum-k]
            hmap[psum] += 1
        return ct