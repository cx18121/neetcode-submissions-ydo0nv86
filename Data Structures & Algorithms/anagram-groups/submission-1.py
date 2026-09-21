from collections import defaultdict
class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        dicts = defaultdict(int)
        for string in strs:
            d = defaultdict(int)
            for ch in string:
                d[ch] +=1
            t = tuple(sorted(d.items()))
            ind = dicts.get(t, -1)
            if (ind >= 0):
                out[ind].append(string)
            else:
                out.append([string])
                dicts[t] = len(out) - 1
        return out


        