class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        ok_list=[0]
        
        for i in range(len(s)):
            for now in ok_list:                
                if s[now:i+1] in wordDict:
                    ok_list.insert(0,i+1)
                    break
        
        if ok_list[0]==len(s):
            return True
        else:
            return False
