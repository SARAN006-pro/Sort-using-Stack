class Sorting:
    def __init__(self,size):
        self.size=size
        self.stack = []
        
    def push(self):
        num_element = int(input("Enter the number of element: "))
        if len(self.stack)+num_element > self.size:
            print("Stack is overflow")
        else:
            for _ in range(num_element):
                element =input("Enter the element: ")
                self.stack.append(element)
                
    def display(self):
        if not self.stack:
            print("Stack is Empty")
            
        else:
            print("The Stack Elements are: ")
            for i in range(len(self.stack)-1,-1,-1):
                print(f"{self.stack[i]}")
            
    def sort_stack(self):
        temp_stack = []
        while self.stack:
            temp = self.stack.pop()
            while temp_stack and temp_stack[-1]>temp:
                self.stack.append(temp_stack.pop())
            temp_stack.append(temp)  
        self.stack = temp_stack
        
obj = Sorting(10)
obj.push()
obj.display()
print("After Sort The Stack:")
obj.sort_stack()
obj.display()