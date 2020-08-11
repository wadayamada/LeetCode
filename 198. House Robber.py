class Solution:
    def rob(self, nums: List[int]) -> int:
        r=0
        nr=0
        
        for n in nums:
            r_=r
            nr_=nr
            
            r=nr_+n
            nr=max(nr_,r_)
            
        return max(nr,r)
