import numpy as np

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x>0:
        
            log=n*np.log(x)
        
            return np.exp(log)
        
        elif x==0:
            
            return 0
        
        else:
            
            log=n*np.log(x*-1)
            
            if n%2==0:
                return np.exp(log)
            
            else:
                return np.exp(log)*-1
            
