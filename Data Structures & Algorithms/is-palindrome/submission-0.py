class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = ""
        for i in s:
            if i.isalnum():
              an += i.lower()

        for i, n in enumerate(an):
            if n != an[len(an)-i-1]:
                return False
        return True  