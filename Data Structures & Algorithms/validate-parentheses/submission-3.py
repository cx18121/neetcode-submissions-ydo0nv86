class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {')' : '(', '}' : '{', ']' : '['}
        for i in s:
            if i in m:
                if not st or m[i] != st.pop():
                    return False 
            else:
                st.append(i)
        return len(st) == 0