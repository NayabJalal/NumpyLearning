import numpy as np

#1d --> 
arr_1d = np.array([1, 2, 3, 4])
print(arr_1d, type(arr_1d))

#2D--->
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print(arr_2d, type(arr_2d))


# dtype -->>
arr = np.array([1 , 3, 5, 7] , dtype= float) # bool -> boolean (0 > false, non zero > true)
print(arr, type(arr))

np.arange(1 , 11 , 2) # (1 , 3, 5 ,7 ,9)

np.arange(1 , 13).reshape(3 , 4) # 1 to 12 -> reshape to 3 rows and 4 cols as ---->>>> [1,2,3,4] [5,6,7,8] [9,10,11,12]

np.arange(1 , 13).reshape(5 , 5) # wrong error 

np.ones((3 , 4)) 

np.zeros((3 , 4))

np.random.random((3 , 4))

np.linspace(-10 , 10 , 10)

np.identity(3)
