class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        data={}
        for i in nums:
            if i not in data.keys():
                data[i]=1
            else:
                data.pop(i)
        
        return list(data.keys())[0]
