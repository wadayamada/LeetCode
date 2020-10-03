class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        def add(x):
            return x[0]+x[1]        
                
        result=sorted([[i,j] for i in nums1 for j in nums2],key=add)        
                                
        return result[:k]
