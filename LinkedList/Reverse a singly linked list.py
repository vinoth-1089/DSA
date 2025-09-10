class Node:
    def __init__(self,data):
        
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        
        self.head=None
        
    def insert(self,data):
        
        newNode=Node(data)
        
        if self.head is None:
           self.head=newNode
           return
        current=self.head
      
        while(current.next):
            current=current.next
        current.next=newNode
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
ll = SinglyLinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Original List:")
ll.display()

ll.reverse()
print("Reversed List:")
ll.display()