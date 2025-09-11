class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
 
        
class LinkedList:
    def __init__ (self):
        self.head=None
        
    def insert_end(self,data):
        
        new_Node=Node(data)
        new_Node.next=self.head
        self.head=new_Node

        
    def display(self):
        current=self.head
        
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print(None)
if __name__ == '__main__':
    
    obj=LinkedList()
    obj.insert_end(10)
    obj.display()
    