class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        
        new_Node = Node(data)
        
        if self.head is None:
            self.head = new_Node
            return
        last = self.head
        
        while last.next:
            last = last.next
        last.next = new_Node

    def search(self, val):
        
        current = self.head
        
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def delete(self, val):
        
        current = self.head
        prev = None

        if current is None:
            return

        if current.data == val:   
            self.head = current.next
            current = None
            return

        while current:            
            if current.data == val:
                prev.next = current.next
                current = None
                return
            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

    print("Search 30:", ll.search(30))   
    print("Search 60:", ll.search(60))  

    ll.delete(30)  
    ll.display()    

    ll.delete(10)   
    ll.display()    
