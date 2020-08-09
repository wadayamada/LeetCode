# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA==None or headB==None:
            return None
        
        else:
            a_count=0
            b_count=0
            
            a_pointer=headA
            b_pointer=headB
            
            while True:
                if a_pointer.next==None:
                    break
                
                a_pointer=a_pointer.next
                a_count+=1
            
            while True:
                if b_pointer.next==None:
                    break
                
                b_pointer=b_pointer.next
                b_count+=1
                                        
            diff=abs(b_count-a_count)
            
            a_pointer=headA
            b_pointer=headB
                        
                        
            if b_count>a_count:
                for a in range(diff):
                    b_pointer=b_pointer.next
            if b_count<a_count:
                for a in range(diff):
                    a_pointer=a_pointer.next                                
            
            while True:
                if b_pointer==a_pointer:
                    return b_pointer
                
                if b_pointer.next==None or a_pointer.next==None:
                    return None
                
                b_pointer=b_pointer.next
                a_pointer=a_pointer.next
