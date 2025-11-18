# create an array of even numbers from 10 to 50


import numpy as np

arr=np.arange(10,51,2)

print(arr)


#create a one dimensional array of 12 elements
print("=====================================================================")
arr_1=np.arange(1,13)

print(arr_1)

print(arr_1.reshape(3,4))


# find the mean,median and std of the above array

print("=====================================================================")
print(np.mean(arr_1))

print(np.std(arr_1))

print(np.median(arr_1))



# create  two 3 by 2 matrix and peform addition and multiplication of two

print("=====================================================================")
array_1=np.random.randint(1,50,size=(3,2))

array_2=np.random.randint(1,50,size=(3,2))

print(np.add(array_1,array_2))

print(np.multiply(array_1,array_2))


# create a 3 by 5 matrix and multiply all elements with 2 and extract right corner 2 by 2 matrix

print("=====================================================================")
a=np.random.randint(1,50,size=(3,5))

a=a*2

print(a)

print(a[0:2,3:])