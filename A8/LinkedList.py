class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
    
    def insert(self, index, value):
        new = Node(value)
        len = self.size()

        if(index<0 or index>len):
            print("Out of range)")
            return
            
        if index == 0:
            new._next = self._first
            self._first = new
        else:
            count = 0
            temp = self._first
            while(count<index-1):
                temp = temp._next

            new._next = temp._next
            temp._next = new



    def remove(self, value):
        if not self._first:
            return 
        if(self._first.value == value):
            self._first = self._first.next
            return
            
        temp = self._first

        while temp._next:
            if(temp._next.value == value):
                temp.next = temp._next._next
                return
            temp = temp._next



l1 = LinkedList()

print(l1.info())

for value in [2,3,9,2,6]:
    l1.append(value)

print('size', l1.size())

print(l1.info())

def get(list,index):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        return n._value
    
get(l1,2)

LinkedList.get=get

l1.get(3)

def set(list,index,value):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        n._value=value

LinkedList.set=set


l2=LinkedList()
for i in range(5):
    l2.append(i)
    
for i in range(l2.size()):
    print(l2.get(i))
    l2.set(i, i*10)

print(l2.info())

l1.insert(1,90)
print(l1.info())
