import numpy

list1=[1,2,3,4]
list2=[5,6,7,8]

array1=numpy.array(list1)
array2=numpy.array(list2)

print(array1)
print(array2)

print(array1 * array2)

# Display division,addition,substraction among these arrays

print(array1 - array2)
print(array1 / array2)
print(array1 + array2)

# .ipynb integrated python notebook used to run code in parts (units)
# .py python file

n=int(input("Enter the limit : "))

odd_numbers=[i for i in range(1,n+1) if i%2!=0]

print(odd_numbers)