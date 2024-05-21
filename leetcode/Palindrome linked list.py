
#https://leetcode.com/problems/palindrome-linked-list/description/

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next



class LinkedList:
    def __init__(self):
        self.head=None



    def append_to_the_end(self,val):

        if self.head is None:
            self.head=Node(val)
            return

        current=self.head

        while current.next!=None:
            current=current.next

        current.next=Node(val)

    def append_to_the_beginning(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=Node(val)
            return
        current=self.head
        new_node.next=current
        self.head=new_node
    def reversing_ll(self):

        prev=None
        current=self.head
        while current.next!=None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node


    def copied_and_reversed_list(self):
        copied_ll=LinkedList()

        current=self.head
        while current!=None:
            copied_ll.append_to_the_beginning(current.val)
            current=current.next

        return copied_ll

    def is_palindrome(self):
        reversed_ll=self.copied_and_reversed_list()

        current_reversed=reversed_ll.head
        current_orginal=self.head

        while current_orginal is not None and current_reversed is not None:
            if current_orginal.val != current_reversed.val:
                return False

            current_orginal=current_orginal.next
            current_reversed=current_reversed.next

