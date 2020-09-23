class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        result_dict={0:0}
        
        for c in coins:
            for i in range(1,amount+1):
                if i-c in result_dict:                    
                    
                    if i in result_dict:
                        result_dict[i]=min(result_dict[i],result_dict[i-c]+1)                    
                    else:
                        result_dict[i]=result_dict[i-c]+1
                                
        
        if amount not in result_dict:
            return -1
        
        
        return result_dict[amount]
