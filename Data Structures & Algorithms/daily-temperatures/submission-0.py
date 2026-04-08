class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            print(stack, res)
            n = temperatures[i]
            while len(stack) > 0 and n > stack[-1][0]:
                tmp = stack.pop()
                res[tmp[1]] = i - tmp[1]
            stack.append((n, i))
        return res
                