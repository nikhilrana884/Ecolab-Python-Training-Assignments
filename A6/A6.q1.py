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
    

        

    def get(self, pos):
        len = self.size()
        if(pos<0 or pos>=len):
            print("Out of range)")
            return
        i = 0
        temp = self.head

        while(i<pos):
            temp = temp.next
            i +=1 

        return temp.value


    def set(self, pos,value):
        len = self.size()
        if(pos<0 or pos>=len):
            print("Out of range)")
            return
        
        i = 0
        temp = self.head

        while(i<pos):
            temp = temp.next
            i +=1 

        temp.value = value


    def size(self):
        len = 0
        temp = self.head

        while temp:
            len += 1
            temp = temp.next

        return len


    def info(self):
        len = self.size()
        print('Linked List of size {len}:')
    
        temp =self.head
        while temp :
            print(temp.value, end="->")
            temp = temp.next
        print("None")

        
    
    def remove(self, value):
        if not self.head:
            return 
        if(self.head.value == value):
            self.head = self.head.next
            return
        
        temp = self.head

        while temp.next:
            if(temp.next.value == value):
                temp.next = temp.next.next
                return
            temp = temp.next


    def clear(self):
        self.head = None


L = LinkedList()

L.append(10)
L.append(20)
L.insert(30,1)

print(L.size())

L.set(1,50)
L.remove(50)

L.info()
