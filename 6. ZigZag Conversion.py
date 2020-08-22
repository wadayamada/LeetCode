class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s
        
        s_dict={}
        for a in range(numRows):
            s_dict[a]=""
            
        #print(s_dict)
        
        number=0
        i_or_d=True
        
        for i in range(len(s)):
            
            s_dict[number]+=s[i]
            #print(s_dict)
            if i_or_d==True and number==numRows-1:
                i_or_d=False
            
            if i_or_d==False and number==0:
                i_or_d=True
            
            
            if i_or_d:
                number+=1
            else:
                number-=1
            
        result=""
        for sd in s_dict:
            result+=s_dict[sd]
            
        
        return result
