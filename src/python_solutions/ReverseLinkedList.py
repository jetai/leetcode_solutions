# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Implementation here can be used a stack to store the values as we
# traverse the singly linked list, and then create a new linked list by
# setting the next values to the popped stack values.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def debugReverseList(self, node):
        while node.val != None:
            print(node.val)
            if node.next == None:
                break
            else:
                node = node.next

    def populateValueStack(self, node):
        val_stack = []
        while node != None and node.val != None:
            val_stack.append(node.val)
            if node.next == None:
                break
            else:
                node = node.next
        return val_stack

    def createReverseList(self, head, node, val_stack):
        if len(val_stack) == 0:
            return head
        else:
            if node is None:
                node = ListNode(val_stack.pop())
                head = node
            else:
                node.next = ListNode(val_stack.pop())
                node = node.next

            return self.createReverseList(head, node, val_stack)

    def reverseList(self, head):
        val_stack = self.populateValueStack(head)
        return self.createReverseList(None, None, val_stack)

# # Iterative solution:
#     def populateValueStack(self, node):
#         val_stack = []
#         while node != None and node.val != None:
#             val_stack.append(node.val)
#             if node.next == None:
#                 break
#             else:
#                 node = node.next
#         return val_stack

#     def createReverseList(self, val_stack):
#         head = None
#         if len(val_stack) > 0:
#             node = ListNode(val_stack.pop())
#             head = node # save pointer to head
#             # Populate reversed linked list
#             while len(val_stack) > 0:
#                 node.next = ListNode(val_stack.pop())
#                 node = node.next
#         return head

#     def debugReverseList(self, node):
#         while node.val != None:
#             print(node.val)
#             if node.next == None:
#                 break
#             else:
#                 node = node.next

#     def reverseList(self, head):
#         val_stack = self.populateValueStack(head)
#         revlist_head = self.createReverseList(val_stack)
#         #self.debugReverseList(revlist_head)
#         return revlist_head
