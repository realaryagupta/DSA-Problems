class Stack:
    def __init__(self,capacity):
        # this will store the capacity of stack
        self.capacity = capacity
        # this variable will store the stack
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty.
        return len(self.stack) == 0

    def push(self, item):
        # checking if elements in stack is more than capacity or not so that we can append accordingly
        if len(self.stack) >= self.capacity:
            print("Stack is full! Insertion is not possible")
            return 
        
        # add item to the end of the list
        self.stack.append(item)
        print(f"inserted {item}")

    def pop(self):
        # Remove and return the top item from the stack.
        if self.is_empty():
            print("Stack is Empty")
            return None
        
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        
        return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    
# Example usage:
if __name__ == "__main__":
    s = Stack(5)  # Create a stack with a capacity of 5

    s.push(10)
    s.push(20)
    print(f"Top element is {s.peek()}")  # Should print 20
    print(f"Stack size is {s.size()}")   # Should print 2

    print(f"{s.pop()} popped from stack")  # Should print 20
    print(f"Top element is {s.peek()}")    # Should print 10