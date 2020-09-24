from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counter={}
        
        order=[]
        
        first_detect={}
        
        for i in range(len(s)):
            if not s[i] in counter:
                counter[s[i]]=1
                order.append(s[i])
                first_detect[s[i]]=i
            else:
                counter[s[i]]+=1
                
            
        for o in order:
            if counter[o]==1:
                return first_detect[o]
            
        return -1
