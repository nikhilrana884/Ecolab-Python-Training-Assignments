import time

def performance_log(fn):
    def inner(*args):
        start = time.time()
        result = fn(*args)
        end = time.time()
        inner.time_taken = end - start
        return result
    return inner

def is_prime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True

@performance_log
def find_primes(mn, mx):
    primes = []
    for n in range(mn, mx):
        if is_prime(n):
            primes.append(n)
    return primes

x = find_primes(2, 50000)
print(x)
print(len(x))

print(f"Time taken:{find_primes.time_taken}") 