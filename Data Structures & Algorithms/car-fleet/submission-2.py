class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hmap = {}
        for i in range(len(position)): 
            hmap[position[i]] = speed[i]
        position = sorted(position)

        n = len(speed)
        # 0 3 5 8 10
        # 1 3 1 4 2 

        # 12, 3, 7, 1, 1
        prev = time = (target - position[n-1]) / hmap[position[n-1]]
        res = 1
        for i in range(n-2, -1, -1):
            time = (target - position[i]) / hmap[position[i]]
            if time > prev:
                res += 1
                prev = time
        return res
