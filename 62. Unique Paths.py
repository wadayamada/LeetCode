class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cal=[]
        
        for i in range(m):
            
            cal.append([])
            
            for j in range(n):
                
                if i==0 and j==0:
                    cal[i].append(1)
                    
                elif j==0 or i==0:
                    cal[i].append(1)
                    
                else:
                    cal[i].append(cal[i][j-1]+cal[i-1][j])
                    
        
        return cal[m-1][n-1]
