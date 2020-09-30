class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        count=[0]
        
        def check(i,j):
            
            grid[i][j]=2
            count[0]+=1
            
            if i-1>=0:
                if grid[i-1][j]==1:
                    check(i-1,j)
                    
            if j-1>=0:
                if grid[i][j-1]==1:
                    check(i,j-1)
                    
            if i+1<len(grid):
                if grid[i+1][j]==1:
                    check(i+1,j)
            
            if j+1<len(grid[0]):
                if grid[i][j+1]==1:
                    check(i,j+1)                        
                
        
        max_count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==0:
                    continue
                    
                elif grid[i][j]==2:
                    continue
                    
                elif grid[i][j]==1:
                    count[0]=0
                    check(i,j)
                    
                    if count[0]>max_count:
                        max_count=count[0]
                                               
        return max_count
