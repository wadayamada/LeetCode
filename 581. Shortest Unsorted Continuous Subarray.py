class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        sortednums=sorted(nums)
        
        if sortednums==nums:
            return 0
                        
        else:
            start=0
            for i in range(len(nums)):
                if sortednums[i]!=nums[i]:
                    start=i
                    break
            
            end=len(nums)-1-1
            for i in range(1,len(nums)):
                if sortednums[i*-1]!=nums[i*-1]:
                    print(i)
                    end=len(nums)-i
                    break
                    
        print(end,start)
                
                    
        return end-start+1
