class solution:
    
    def allocate_pages(self,books,students):
        if students > len(books):
            return -1
        
        low=max(books)
        high=sum(books)
        ans=-1
        while low<=high:
            
            mid =(low+high)//2
            
            if self.find_no_of_students(books,mid)<=students:
                ans=mid
                high=mid-1
            else:
               low=mid+1
        return ans
    def find_no_of_students(self,books,max_pages):
        pages=0
        student=1
        
        for page in books:
            if page+pages >max_pages:
                student+=1
                pages=page
            else:
                pages+=page
        return student
sol = solution()
books = [12, 34, 67, 90]
students = 2
print(sol.allocate_pages(books, students))  
