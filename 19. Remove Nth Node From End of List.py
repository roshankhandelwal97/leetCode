#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        leng = 0
        prev = head
        curr = prev.next
        count = 0

        #find length of list
        while(temp!=None): 
            leng +=1
            temp = temp.next
            
        #if len of list = 1
        if(leng == 1):
            return None

        #if we need to delete the first element
        if leng == n: 
            head = curr

        leng = leng - n

        #main logic
        while(count != leng and curr!= None):
            if(count == leng - 1):
                prev.next = curr.next
            count +=1
            prev = prev.next
            curr = curr.next
        return head

        
        
