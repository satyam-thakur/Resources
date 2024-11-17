class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        hashset = set(nums)
        res = []
        for i in range(1,n+1):
            if i not in hashset:
                res.append(i)
        return res
    
print(Solution.findDisappearedNumbers(None,[4,3,2,7,8,2,3,1]))
