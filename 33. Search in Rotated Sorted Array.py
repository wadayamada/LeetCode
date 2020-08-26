class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        
        ma=max(nums)
        ma_i=nums.index(m)
                                
        start_i=(ma_i+1)%len(nums)
        end_i=ma_i
        
        if end_i<start_i:
            end_i+=len(nums)
            
        print(start_i.end_i)
        
        """
        
        if target in nums:
            return nums.index(target)
        
        else:
            return -1
        
