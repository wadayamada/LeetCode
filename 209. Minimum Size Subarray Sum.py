class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        
        result=0
        
        for i in range(len(nums)):
            n=nums[:i+1]            
            
            if result==0:
                if sum(n)>=s:
                    result=len(n)
                    
            if result!=0:
                
                check_n=n[len(n)-(result-1):]                
                
                if sum(check_n)>=s:
                    while sum(check_n)>=s:
                        check_n=check_n[1:]
                        
                    result=len(check_n)+1
                            
        return result
