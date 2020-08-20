class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        if len(s)==0:
            return result
        
        sub_s=s[0]
        now_result=len(sub_s)
        result=max(result,now_result)
        
        #print(result)
        
        for i in range(1,len(s)):
            if not s[i] in sub_s:
                sub_s+=s[i]
                
            
            else:
                sub_s=sub_s[sub_s.index(s[i])+1:]+s[i]
                
            now_result=max(now_result,len(sub_s))
            result=max(result,now_result)
            print(sub_s)
            
        return result
            
