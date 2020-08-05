class Solution:
    def climbStairs(self, n: int) -> int:
        way_dict={}
        way_dict[1]=1
        way_dict[2]=2
        if n==1:
            return way_dict[1]
        elif n==2:
            return way_dict[2]
        else:
            result=0
            for a in range(3,n+1):
                way_dict[a]=way_dict[a-1]+way_dict[a-2]
                if a==n:
                    return way_dict[a]
