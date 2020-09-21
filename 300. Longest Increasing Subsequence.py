class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        length_dict={}
        
        for i in range(len(nums)):
            now=nums[i]                            
            small_list=[n for n in nums[:i] if n<now]            
            
            if len(small_list)>0:            
                length_dict[now]=max([length_dict[s] for s in small_list])+1
            else:
                length_dict[now]=1
            
            
        return max(length_dict.values())
