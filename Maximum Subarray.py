#全探索
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=nums[0]
        for n in range(len(nums)):
            sum=0
            for m in range(len(nums)-n):
                sum+=nums[n+m]
                if sum>max:
                    max=sum
        return max
"""

#https://qiita.com/76b26e64/items/2f9ec0f32ebb4508dc2e
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        global_max=local_max=nums[0]
        
        for a in range(1,len(nums)):
            local_max=max(local_max+nums[a],nums[a])
            global_max=max(local_max,global_max)
        
        return global_max
