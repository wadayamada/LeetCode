def trade(nums,a,b):
    n=nums[a]
    nums[a]=nums[b]
    nums[b]=n

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)==1:
            pass
        
        elif len(nums)==2:
            trade(nums,0,1)
        
        
        else:
            
            if nums==sorted(nums,reverse=True):
                trade(nums,nums.index(min(nums)),0)
                nums[1:]=sorted(nums[1:])
            
            
            else:
            
                for i in range(2,len(nums)+1):
                    if nums[i*-1:]==sorted(nums[i*-1:],reverse=True):
                        continue
                
                    else:
                        now=nums[i*-1:]                    
                        t=min([a for a in now[1:] if a>now[0]])
                        now_i=now.index(t)
                        trade(now,0,now_i)
                        now[1:]=sorted(now[1:])
                        print(now,t,now_i)
                    
                        nums[i*-1:]=now
                    
                        break
                
            print(nums)
