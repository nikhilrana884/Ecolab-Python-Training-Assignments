n = int(input("Enter the number of elements:"))


largest = -999998
second_largest = -9999995

if( n<=1 ):
    print("n less than 2")
    
for i in range(1,n+1):
   l=int(input())

   if l>second_largest:
        if l>largest:
            second_largest=largest
            largest=l
        else:
            second_largest=l



print("Second largest num is", second_largest)