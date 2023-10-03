
class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self, *args):
        self._first=None
        self._last=None
        self.append(*args)

    def append(self, *args):
        for value in args:
            self._append(value)


    def _append(self, value):
        n = Node(value)
        if self._first==None: # list is empty
            self._first=n
            self._last=n
        else: # add to the end of a non-empty list
            self._last._next = n
            n._previous = self._last
            self._last = n

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
    
    def list_sum(self):
        temp = self._first
        total_sum = 0

        while temp is not None:
            total_sum += temp._value
            temp = temp._next

        return total_sum
        
    
    def find_primes(self):
        primes = []
        temp = self._first

        while(temp):
            num = temp._value
            if (is_prime(num)):
                primes.append(num)

            temp = temp._next
        return primes
    
    def find_even(self):
        even = []
        temp = self._first

        while(temp):
            num = temp._value
            if (num%2 ==0):
                even.append(num)

            temp = temp._next
        return even

    def brute_sort(self):
        sorted = LinkedList()
        curr = self._first
        while curr:
            temp = curr._next
            while temp:
                if temp._value < curr._value:
                    temp._value, curr._value = curr._value, temp._value
                    
                temp = temp._next

            sorted.append(curr._value)
            curr = curr._next

        return sorted

    def quick_sort(self):
        pass
        
        

                

    
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n/2)+1):
        if(n % i) == 0:
            return False
    
    return True

    

    

l=LinkedList()
for x in [9,1,8,2,6]:
    l.append(x)

print(l)
#print(len(l))

'''

for i in range(len(l)):
    print(l[i])
    l[i]*=3

print(l)

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

max=1000

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


start=time.time()
sum=l.list_sum()
end=time.time()
print(f'sum is {sum}')
print(f'Total time taken to sum list is {end-start}')

'''
primes = l.find_primes()
print(primes)

evens = l.find_even()
print(evens)

s = l.brute_sort()
print(s)

q = l.quick_sort()
print(q)