class Solution:
    def myAtoi(self, str: str) -> int:
        i=str.split()
                        
        
        digits_list=["0","1","2","3","4","5","6","7","8","9"]
        
        if str=="" or str=="+" or str=="-" or str==" " or len(i)==0 or str[:2]=="+-" or str[:2]=="-+":
            return 0
        
        if i[0][0]=="+":
            
            result="+"        
            for p in range(1,len(i[0])):                
                if i[0][p] in digits_list:
                    result+=i[0][p]                    
                else:
                    break
                                    
            if result=="+":
                return 0
            
            result=int(result)            
            
            if result<=2**31-1:
                return result
            else:
                return 2**31-1
            
        elif i[0][0]=="-":
                                    
            result="-"        
            for p in range(1,len(i[0])):                
                if i[0][p] in digits_list:
                    result+=i[0][p]                    
                else:
                    break
            
            #result=int(i[0][1:])*-1
            if result=="-":
                return 0
            print(result)
            result=int(result)
            
            if result>=(2**31)*-1:
                return result
            
            else:
                return (2**31)*-1
            
                    
        elif i[0][0] in digits_list:
            
            if not "." in i[0]:
                
                result=""
                for p in range(len(i[0])):                
                    if i[0][p] in digits_list:
                        result+=i[0][p]            
                    else:
                        break
                        
                result=int(result)
                
                if result<=2**31-1:
                    return result
                else:                    
                    return 2**31-1
                                
            else:                
                ten=i[0].index(".")
                return int(i[0][:ten])
                    
        else:
            return 0
