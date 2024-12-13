class Stack:

    def __init__(self, items = [], limit = 100):
        pass
        self.items = items
        self.limit = limit


    def isEmpty(self):
        pass
        if len(self.items) == 0:
            return True
        else:
            return False


    def push(self, item):
        pass
        if self.full():
            return None
        else: 
            self.items.append(item)

    def pop(self):
        pass
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass
        return len(self.items) >= self.limit

    def search(self, target):
        pass
        if target in self.items:
            index = self.items.index(target)
            return (len(self.items)-1) - index
        else:
            return -1
