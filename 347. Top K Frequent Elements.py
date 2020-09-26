import collections 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result=collections.Counter(nums)
        result=sorted(result.items(),key=lambda x:x[1],reverse=True)        
        
        rdv=list(dict(result).keys())
        
        result_list=[]
        for i in range(k):
            result_list.append(rdv[i])
        return result_list
    
