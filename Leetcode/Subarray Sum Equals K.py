class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = {0: 1}

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res
    
print(Solution().subarraySum([1,1,1,-1,2,4], 3))
print(Solution().subarraySum([1,1,1,-1,2,4], 2))
print(Solution().subarraySum([1,2,3], 3))
