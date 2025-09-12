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
    
    def search(self,val):
        current=self.head
        cnt=1
        while current:
            if current.data == val:
                print(f"Search present at {cnt} Node:",val)
                return
            current=current.next
            cnt+=1
  
        print(f"{val} not found in the list.")
    def display(self):
        current=self.head
        
        while current:
            print(current.data,end=' -> ')
            current=current.next
        print("None")
        
        

if __name__=='__main__':
    
    obj=LinkedList()
    n=int(input("Enter no.of Elements:"))
    for i in range(1,n+1):
        m=int(input(f"Enter  Elements Node {i}:"))
        obj.append(m)
    obj.display()
    
    obj.search(5)