class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tfreq = {}
        ret = []
        ct = 0

        for word in strs:
            freq = {}
            for ch in word:
                freq[ch] = freq.get(ch, 0) + 1
            freq = tuple(sorted(freq.items()))
            if freq in tfreq:
                ret[tfreq[freq]].append(word)
            else:
                tfreq[freq] = ct
                ret.append([word])
                ct += 1
        return ret