class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                        
        if len(prices)==0:
            profit=0
            
        else:
            profit=0
            
            buy=prices[0]
            
            for price in prices[1:]:
                if price<buy:
                    buy=price
                if price-buy>profit:
                    sell=price
                    profit=sell-buy                    
        
        return profit
