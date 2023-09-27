class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
    
    def append(self,value):
        new = Node(value)

        temp = self.head

        if not temp:
            self.head = new
        else:
            while temp.next:
                temp = temp.next

            temp.next = new 
    
    def insert(self, value, pos):
        new = Node(value)
        len = self.size()

        if(pos<0 or pos>len):
            print("Out of range)")
            return
        
        if pos == 0:
            new.next = self.head
            self.head = new
        else:
            count = 0
            temp = self.head
            while(count<pos-1):
                temp = temp.next

            new.next = temp.next
            temp.next = new
    

        

    #def get():

    #def set():

    def size(self):
        len = 0
        temp = self.head

        while temp:
            len += 1
            temp = temp.next

        return len


    #def info():

    #def remove():

    def clear(self):
        self.head = None


L = LinkedList()

L.append(10)
L.append(20)
L.insert(30,1)

print(L.size())
