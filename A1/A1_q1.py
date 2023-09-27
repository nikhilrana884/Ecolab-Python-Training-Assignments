largest = -99999

n = int(input("Enter the number of elements:"))

if( n<=0 ):
    print("n less than 0")
   
for i in range(1,n+1):
   l=int(input())
   if l>largest:
        largest=l

print("largest num is", largest)
