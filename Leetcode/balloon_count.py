class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # c = collections.Counter(text)
        c = {}
        for t in text:
            c[t] = 1 + c.get(t,0)
        return min(c['b'],c['a'],c['l']//2,c['o']//2,c['n'])
    
print(Solution().maxNumberOfBalloons("nlballoonaebolko"))
