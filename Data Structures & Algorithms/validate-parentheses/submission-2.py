class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.append(i)
            if len(st) == 0:
                return False
            elif i == ')':
                if st.pop() != '(':
                    return False
            elif i == ']':
                if st.pop() != '[':
                    return False
            elif i == '}':
                if st.pop() != '{':
                    return False
        return len(st) == 0
        