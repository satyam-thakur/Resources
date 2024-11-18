class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    
print (Solution.singleNumber(None,[4,1,2,1,2]))
