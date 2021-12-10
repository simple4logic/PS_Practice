from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None #define address of reverse string as null
        slow = fast = head #set start point

        while fast and fast.next: #when both are true
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            #making reverse linked list until the middle point
        if fast:
            slow = slow.next #when odd length, move one more

        while rev and (rev.val==slow.val):
            slow, rev = slow.next, rev.next #next node
        return not rev
        '''
        do it until rev reaches the end or not palindrome 
        when reaches the end, rev is none. It means palindrome so rev = 
        '''
'''
rev <- slow
rev.next <- rev
slow <- slow.next

'''

#to test, you have to make to linked-list manually. 
inp = [1,2,2,1] #inp = input as head
node3 = ListNode(inp[3])
node2 = ListNode(inp[2], node3)
node1 = ListNode(inp[1], node2)
head = ListNode(inp[0], node1)


#for test
a = Solution()
a.isPalindrome(head)