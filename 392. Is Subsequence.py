class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)==0:
            return True
        
        if len(t)==0:
            return False
        
        
        i=0
        goal=len(s)
        
        for ti in t:
            if ti==s[i]:
                i+=1
                
            if i==goal:
                return True
            
        return False
            
        
