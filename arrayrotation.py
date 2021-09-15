# program for array rotation
def rotateArrayLeft(a,r,n):
    for i in range(r):
        firstval=a[0]
        for i in range(n-1):
                a[i]=a[i+1]
        a[n-1]=firstval
#array input for user
a= [1, 2, 3, 4, 5, 6, 7]
n=int(input("enter number of elements of the array:"))
a=[]
print("enter number of array:")
for i in range(n):
    numbers=int(input())
    a.append(numbers)
r=int(input("enter rotation count:"))
#printing array
print("initial array:",end=" ")
for i in range(n):
    print("%d"%a[i],end=" ")
rotateArrayLeft(a,r,n)
print("\n array after rotation:",end=" ")
for i in range(n):
    print("%d"%a[i],end=" ")
