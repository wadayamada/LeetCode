class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        emails_list=[]
        
        for e in emails:
            mark=e.index("@")
            localname=e[:mark]
            domainname=e[mark+1:]
            
            result=""
            
            for ln in localname:
                
                if ln==".":
                    continue
                    
                elif ln=="+":
                    break
                    
                else:                
                    result+=ln
                    
            result+="@"
            result+=domainname
            
            if not result in emails_list:
                emails_list.append(result)
            
        return len(emails_list)
                
            
