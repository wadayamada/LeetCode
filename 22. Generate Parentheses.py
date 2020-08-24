def ok_judge(s):
    
    s_list=[]
    
    for a in s:
        
        
        
        if a=="(":
            s_list.append(a)
            
        elif a==")":
            
            if len(s_list)==0:
                return 0
            
            s_list.pop()
        
    if len(s_list)==0:
        return 1
    else:
        return 0
            

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        option=["(",")"]
        
        result=[]
        
        for a in range(2**(n*2)):
            data=""
            for b in range(n*2):
                if (a>>b)&1==1:
                    data+=option[0]
                else:
                    data+=option[1]
                    
            
                    
            if ok_judge(data):
                print(data)
                result.append(data)
                
        
        return result
