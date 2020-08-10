class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data={}
        for n in nums:
            if n not in data.keys():
                data[n]=1
            else:
                data[n]+=1
        
        max_count=max(data.values())
        
        result_list=[k for k, v in data.items() if v == max_count]
        
        return result_list[0]
