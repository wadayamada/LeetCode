class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)==0:
            return nums
                            
        for i in range(len(nums)):
            
            #print(nums)
            
            if i==0:
                print("continue")
                continue
                
                        
            elif nums[i]==0:
                print("continue")
                continue
                
                        
            else:
                j=i-1
                check=True
                while check:
                    if nums[j-1]!=0 or j==0:
                        check=False
                    if check:
                        j=j-1                        
                
                if nums[j]==0:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                
                
                
        return nums
