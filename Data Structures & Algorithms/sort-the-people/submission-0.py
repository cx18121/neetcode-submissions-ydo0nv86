class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        s = [(heights[i], names[i]) for i in range(n)]
        s.sort(reverse=True)
        ret = [i[1] for i in s]
        return ret