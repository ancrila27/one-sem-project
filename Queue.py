## Implementation of a Queue in Python.

class Queue:
    def __init__(self):
        self.items = []
        print("a queue has been created")

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
##        print("one item has been added to the queue")
##        self.show_items()

    def dequeue(self):
        return self.items.pop()   #removes the last item from list

    def size(self):
        return len(self.items)

    def consume(self): #consume 10 items from list
        if self.size() >= 10:
            print("Consuming first 10 items")
            c = self.items[:-11:-1]
            del self.items[:-11:-1] 
            return c 
        else:
            print("not enough items yet")

    def consumeQ(self, num_items):
        if self.size() >= num_items:
            c = self.items[:-num_items:-1]
            del self.items[:-num_items:-1]
            return c
        else:
            print("ERROR")

    def isEmpty(self):
        if ( len(self.items) > 0 ):
            return true
        else:
            return false

    def show_items(self):
        print(self.items, end="\n")
##        for i in range(len(self.items)):
##            print(self.items[i])

    
    
