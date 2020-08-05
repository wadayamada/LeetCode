class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            search=target-nums[a]
            if search in nums:
                b=nums.index(search)
                if not a==b:
                    return [a,nums.index(search)]

#総当たり
#時間オーバーでダメ
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(len(nums)):
                if not a==b:
                    if nums[a]+nums[b]==target:
                        return [a,b]
"""
