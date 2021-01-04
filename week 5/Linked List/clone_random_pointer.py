# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # T: O(N) | S: O(N)
    def copyRandomList(self, head: 'Node') -> 'Node':

        curr = head
        dup_head = None
        dup_curr = None

        while curr != None:
            n_node = Node(curr.val, None, None)

            if dup_head == None:
                dup_head = n_node
                dup_curr = n_node
            else:
                dup_curr.next = n_node
                dup_curr = n_node

            curr = curr.next

        curr = head
        dup_curr = dup_head
        while dup_curr != None:
            nxt = curr.next
            curr.next = dup_curr

            dup_curr.random = curr

            dup_curr = dup_curr.next
            curr = nxt

        dup_curr = dup_head
        while dup_curr != None:
            if dup_curr.random.random != None:
                dup_curr.random = dup_curr.random.random.next
            else:
                dup_curr.random = None
            dup_curr = dup_curr.next

        return dup_head

    # T: O(N) | S: O(1)
    def copyRandomList2(self, head):

        curr = head
        while curr != None:
            n_node = Node(curr.val, None, None)
            nxt = curr.next

            curr.next = n_node
            n_node.next = nxt

            curr = nxt

        curr = head
        while curr != None:
            if curr.random != None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        og = head
        cp = head.next
        res = head.next
        while cp.next != None:
            og.next = og.next.next
            cp.next = cp.next.next

            og = og.next
            cp = cp.next

        return res