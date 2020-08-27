class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result=[]
        
        def search(now,t,global_i):            
            
            if t==0:                
                result.append(list(now))                
                return                    
            
            for i in range(global_i,len(candidates)):
                
                if t>=candidates[i]:
                    now.append(candidates[i])
                    search(now,t-candidates[i],i)
                    now.pop()                
        
            
        search([],target,0)
        
        return result
               
