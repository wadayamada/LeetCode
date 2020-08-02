class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        
        for a in s:
            if a=="(":
                stack.append("(")
            elif a=="[":
                stack.append("[")
            elif a=="{":
                stack.append("{")
                
            if a==")":
                if len(stack)>0:
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
            elif a=="]":
                if len(stack)>0:
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
            elif a=="}":
                if len(stack)>0:
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            #print(stack)
                    
        if len(stack)==0:
            return True
        else:
            return False
