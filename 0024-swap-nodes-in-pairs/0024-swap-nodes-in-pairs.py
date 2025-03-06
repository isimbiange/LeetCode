# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev, curr = dummy, head 

        while curr and curr.next: #while there is the next node 
            nextPair = curr.next.next  # store the next node after a air of nodes
            second = curr.next    #the second node position will be replaced by the first node 
            

            #swap

            second.next = curr  #the second node will  be equal to the first node 
            curr.next = nextPair  # current start/head node== the second node
            prev.next = second  #the current/first node will be == second nod 
            
            


            #initialize

            prev = curr  #previous means the current node 
            curr = nextPair  #current node will be equal to the next pair 

        return dummy.next  #print out the new linkNode




        