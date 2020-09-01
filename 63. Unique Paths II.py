class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if len(obstacleGrid)==1 and len(obstacleGrid[0])==1:
            if obstacleGrid[0][0]==0:
                return 1
            else:
                return 0                                    
        
        cal=[]
        
        for m in range(len(obstacleGrid)):
            
            cal.append([])
            for n in range(len(obstacleGrid[0])):
                
                if obstacleGrid[m][n]==1:
                    cal[m].append(0)                    
                    
                else:
                    
                    if m==0 and n==0:
                        cal[m].append(1)
                    
                    elif m==0:
                        cal[m].append(cal[m][n-1])
                    
                    elif n==0:
                        cal[m].append(cal[m-1][n])
                        
                    else:
                                                                      
                        cal[m].append(cal[m-1][n]+cal[m][n-1])                                
                        
        return cal[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
        
