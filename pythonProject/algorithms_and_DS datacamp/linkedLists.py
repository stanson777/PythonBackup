class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBEgin(self,data):
        new_Node=Node(data)

        if self.head:
            new_Node.next=self.head
            self.head=new_Node
        else:
            self.head=new_Node


    def insertAtEnd(self,data):
        new_Node=Node(data)

        if self.head is None:
            self.head=new_Node

        current_node=self.head
        while current_node:
            current_node=current_node.next

        current_node.next=new_Node
            