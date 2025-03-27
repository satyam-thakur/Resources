class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2 ,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
print (Solution().climbStairs(6))

'''
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
'''
