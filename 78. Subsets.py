import numpy as np

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        
        for i in range(2**len(nums)):
            
            b=bin(i)[2:]            
            b=([int(a) for a in b])
            b=[0]*(len(nums)-len(b))+b            
            r_l=[nums[i] for i in range(len(nums)) if b[i]!=0]
            result.append(r_l)
                                      
        return result
