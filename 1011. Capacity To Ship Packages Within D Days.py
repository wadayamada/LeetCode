class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        min_num=max(weights)
        max_num=sum(weights)
        
        while min_num<max_num:
            
            days=0
            now_sum=0
            
            mid=int((min_num+max_num)/2)
            
            for i in weights:
                now_sum+=i
                
                if now_sum>mid:
                    
                    now_sum=i
                    days+=1
                    
            
            if days+1<=D:
                
                max_num=mid
                
            else:
                
                min_num=mid+1
                                
        return min_num
                
