class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return chr(10001);
        return chr(1000).join(strs)

    def decode(self, s: str) -> List[str]:
        if s == chr(10001):
            return []
        return s.split(chr(1000))