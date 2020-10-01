class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        result_list=[]
        
        last_len=2**(N-1)
        start=1
        end=last_len
        
        for i in range(N):
            
            if i==0:
                result_list.append(0)
                
            else:
                #右側
                if (end+start)/2<K:
                    if result_list[i-1]==0:
                        result_list.append(1)
                    else:
                        result_list.append(0)
                                            
                    start=int((end+start)/2)+1
                
                #左側
                else:
                    if result_list[i-1]==0:
                        result_list.append(0)
                    else:
                        result_list.append(1)
                        
                    end=int((end+start)/2)
                    
        return result_list[-1]
                
