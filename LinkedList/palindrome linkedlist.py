class Node:
    
    def __init__(self,data):
        
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        
        self.head=None
    
    def append(self,data):
        
        new_Node=Node(data)
        
        if self.head is None:
            self.head=new_Node
            return
        
        current=self.head
        
        while current.next:
            current=current.next
        current.next=new_Node
    
    def display(self):
        current=self.head
        
        while current:
            print(current.data,end=' -> ')
            current=current.next
        print("None")
        
        
        
    def palindrome(self):
        
        prev=None

        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        current = slow
        
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        first_half=self.head
        second_half=prev
        
        while second_half:
            
            if first_half.data!=second_half.data:
                print("Is Not a Palindrome")
                break
            else:
                print("Is a Palindrome ")
                
            first_half=first_half.next
            second_half=second_half.next
        
        
        
if __name__ == "__main__":
    
    obj=LinkedList()
    n=int(input("Enter no.of Elements:"))
    for i in range(1,n+1):
        m=int(input(f"Enter  Elements Node {i}:"))
        obj.append(m)
    obj.display()
    obj.palindrome()
