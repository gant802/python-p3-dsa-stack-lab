import ipdb
class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def __repr__(self):
        return f"Stack({self.items})"

    def isEmpty(self):
        if not self.items:
            return True
        else : 
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            return self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        
    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if not self.isEmpty():
            return True
        else:
            return False

    def search(self, target):
        if self.items[-1] == target:
            return 0
        if target in self.items:
            return (len(self.items) - self.items.index(target)) - 1
        else : 
            return -1
            
stk = Stack([5,6,7,8,9,10])

