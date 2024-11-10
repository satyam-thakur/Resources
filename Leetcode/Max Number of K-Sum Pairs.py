class Solution:
    def maxOperations(self, nums: list[int], k: int) -> (int, list[int]): # type: ignore
        nums.sort()
        l, r = 0, len(nums)-1
        operations = 0
        arr = []
        while l<r:
            #chek if sum of l, r is K, if yes then operation = +1
            sums = nums[l] + nums[r]
            if sums == k:
                operations += 1
                arr.append([nums[l], nums[r]])
                l += 1
                r -= 1
            elif sums < k:
                l += 1
            else:
                r -= 1
        return operations, arr
           
print (Solution.maxOperations(None,[3,1,3,4,3,2],5))

