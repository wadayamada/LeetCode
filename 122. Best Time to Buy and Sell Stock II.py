class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)<2:
            return 0
        
        buy=-1
        result=0
        
        for i in range(len(prices)-1):
            
            if buy<0:
            
                if prices[i]<prices[i+1]:
                    buy=prices[i]
                
            else:
                
                if prices[i]>prices[i+1]:
                    result+=prices[i]-buy
                    buy=-1
                    
        if buy>=0:
            result+=prices[-1]-buy
                    
        return result
                
            
        
