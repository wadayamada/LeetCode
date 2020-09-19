class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        elif len(nums)==3:
            return max(nums)
                
        def check(n):
            pre=0
            cur=0            
            for i in n:
                pre,cur=cur,max(pre+i,cur)            
            return max(pre,cur)                                                            
                    
        first_rob=nums[0]+check(nums[2:-1])
        first_not_rob=check(nums[1:])
        
        
        return max(first_rob,first_not_rob)
