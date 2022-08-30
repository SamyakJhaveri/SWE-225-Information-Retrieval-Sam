class Stack:

    def __init__(self):
        self.item = []
    
    def push(self, num):
        self.item.append(num)
    def pop(self):
        self.item.pop()
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return 0
    def isEmpty(self): 
        return not self.item

if __name__ == "__main__":
    obj = Stack()
    obj.push(1)
    obj.pop()
    obj.push(55)
    print(obj.peek())
    print(obj.size())
    print(obj.isEmpty())