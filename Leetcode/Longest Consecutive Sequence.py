class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        '''Take each element in set
        Check if previous element exists, if not this is start of sequence
        increment the num and check if +1 element exists and increaswe length'''
        longest = 0
        
        for i in nums:
            length = 0
            if i-1 not in numset:
                length += 1
                while i+1 in numset:
                    length += 1
                    i += 1
                longest = max(longest, length)
        return longest
    
print (Solution.longestConsecutive(None, [100,4,200,1,3,2]))
