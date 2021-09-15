# program to split the array and the first part to the end

# Function to split arrays in Python
def splitArray(a, R, n):
    for i in range(R):
    	x = a[0]
    	for i in range(n-1):
    		a[i] = a[i+1]
    	a[n-1] = x

# Taking array input from user
a = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Enter number of elements of the array: "))
a = []
print("Enter elements of the array :")
for i in range(n):
  numbers = int(input())
  a.append(numbers)
R = int(input("Enter position: "))

# Printing array 
print("Initial Array :", end = " ")
for i in range(n):
	print ("%d"% a[i],end=" ")
	
# Calling function for split array 
splitArray(a, R, n)

# Printing new array 
print("\nArray after split: ", end = " ")
for i in range(n):
	print ("%d"% a[i],end=" ")
