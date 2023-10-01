class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self, *args):
        self._first=None
        self.append(*args)

    def append(self, *args):
        for value in args:
            self._append(value)


    def _append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    #def info(self):
    def __str__(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    #def size(self):
    def __len__(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c

    def __locate(self,index):
        if index>=len(self):
            raise IndexError(f'Invalid Index :{index}')
        
        n=self._first
        for i in range(index):
            n=n._next
            
        return n


             
    #def get(self,index):
    def __getitem__(self,index):
        n=self.__locate(index)
        return n._value  #if n else None
    

    #def set(self,index,value):
    def __setitem__(self,index,value):
        n=self.__locate(index)
        n._value=value

    def insert(self, index, value):
        y=self.__locate(index)
        x=y._previous 

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            self._first=new_node

        y._previous=new_node

    def remove(self, index):
        n=self.__locate(index)
        
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            self._first=y

        if y:
            y._previous=x
        return n._value
    

l=LinkedList()
print(l)
print(len(l))

for x in [2,3,9,2,5]:
    l.append(x)

print(l)
print(len(l))


for i in range(len(l)):
    print(l[i])
    l[i]*=3

print(l)


l2=LinkedList(5,9,2,1)
print(l2)

l2.append(8,2,4,1)

print(l2)


def create_list(size):
    l=LinkedList()
    for x in range(1,size+1):
        l.append(x)

    return l


def sum_list(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum

l= create_list(100)
s = sum_list(l)
print(s)

max=50

import time

start=time.time()
l=create_list(max)
end=time.time()
print(f'Total time taken to create list is {end-start}')


start=time.time()
sum=sum_list(l)
end=time.time()
print(f'sum is {sum}')
print(f'Total time taken to sum list is {end-start}')

