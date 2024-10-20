from typing import List


#Time Complexity is O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
#Time Complexity is O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num  
            if complement in seen:  
                return [seen[complement], i]  
            seen[num] = i  

sum=Solution()
result=sum.twoSum([2,3,4,5],9)
print(result)
