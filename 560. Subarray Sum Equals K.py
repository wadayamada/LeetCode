import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        sum_dict=collections.defaultdict(int)
        count=0
        sum_now=0
        
        for n in nums:
            
            sum_now+=n
            check=sum_now-k
            
            if sum_now==k:
                count+=1
                
            count+=sum_dict[check]
                                    
            sum_dict[sum_now]+=1                                                                                            
        return count
            
