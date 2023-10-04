class prime_range:
    def __init__(self, min, max):
        if max is None:
            self._min = 2
            self._max = min
        else:
            self._min = min
            self._max = max
        
    def __iter__(self):
        return self.iterator(self._min, self._max)

    def is_prime(n):
        if n<2: 
            return False
        for i in range(2, int(n/2)+1):
            if n%i == 0: 
                return False
        return n
    
    class iterator:
        def __init__(self, min, max):
            self._max = max
            self._n = min

        def __next__(self):
            self._n += 1
            
            if self._n <= self._max:
                if not prime_range.is_prime(self._n):
                    self.__next__()
                return prime_range.is_prime(self._n)
            else:
                raise StopIteration()

           

for p in prime_range(10, 100):
    print(p, end=' ')

print()

primes = prime_range(10,200)
it = iter(primes)

print(next(it)) #11
print(next(it)) #13
print(next(it)) #17
print(next(it)) #19
print(next(it)) 
print(next(it))
print(next(it))
