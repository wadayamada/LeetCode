def p(nums):
    if len(nums)==0:
        return []
    
    elif len(nums)==1:
        return [nums]
    
    else:
        result=[]
        
        for i in range(len(nums)):
            
            others=nums[:i]+nums[i+1:]
            
            others_result=p(others)
            
            for o_r in others_result:
                result.append(o_r+[nums[i]])
                
        return result
            
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
                          
    
        return p(nums)
