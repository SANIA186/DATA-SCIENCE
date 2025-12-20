#============LIBRARIES===========#

# import numpy as np
# arr = np.array([10,20,30])
# print(arr)

# import numpy as np
# arr = np.zeros([1,2,3])
# print(arr)


#=========METHODS:==========#
# z=np.zeros(5)
# print(z)

# z=np.ones(5)
# print(z)

# ar = np.arange(1,10,2)
# print(ar)

# ar=np.asarray([1,2,3,4,5])
# print(ar)

# ls =np.linspace(1,10,3) 
# print(ls)

# ls =np.linspace(1,10,4)
# print(ls)


# #reshape()
# arr= np.arange(1,7)
# print(arr)
# newarr= arr.reshape(2,3)
# print(newarr)


# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2.ndim)

# arr2 = np.array([[1,2,3],[4,5,6],[7,8,9],[3,5,7],[8,9,5],[8,8,9]])
# print(arr2.ndim)

# import numpy as np

# array_3d = np.array(
#     [
#         [
#             [1, 2],
#             [3, 4]
#         ],
#         [
#             [5, 6],
#             [7, 8]
#         ]
#     ]
# )
# print(array_3d.ndim)
# print(arr2.size)
# print(arr2.dtype)

# a = np.array([7,2,3,4,5,5])
# print(a.size)
# print(a.dtype)
# print(sum(a))
# print(max(a))
# print(min(a))
# print(a.view())
# print(a.copy())
# print(np.sqrt(a))
# print(a.mean())
# print(np.unique(a))
# print(np.sort(a))  

# a= ["l","i","s","t"]
# z= np.asarray(a)
# z[::-1]
# print(z)
# print(z[::-1])
# print(np.flip(z))


# ===============PANDAS===================


import pandas as pd
# s= pd.Series([10,20,30])
# print(s)

# s1=pd.Series([100,200,300],index=["Jaya","sania","rumaiz"])
# print(s1)
# print(s1["sania"])

# S3=[[1,2,3],[4,5,6],[7,8,9]]
# df= pd.DataFrame(S3)
# print(df)

# data ={
#     "Name": ["Jaya","Sania","Rumaiz","xxx","uyyyy","zzzz","aaaa","bbbbb","ccccc","ddddd","eeeee"],
#     "Age": [24,25,26,27,28,29,30,31,32,33,34],
#     "Salary": [10000,20000,30000,40000,50000,60000,70000,8000,90000,100000,110000]

# }
# df1= pd.DataFrame(data)
# print(df1["Salary"])
# print(df1.loc[0])
# print("==================")
# print(df1.loc[1])
# print("==================")
# print(df1.loc[2])


# #Methods
# print(df1.head())
# print(df1.tail())
# print(df1.shape)
# print(df1.columns)
# print(df1.info())


# data={
#     "Department": ["HR","HR","IT","IT","Sales"],
#     "Salary": [10000,20000,30000,40000,50000]
# }
# df= pd.DataFrame(data)
# print(df)
# result= df.groupby("Department")["Salary"].sum()
# print(result)
# result= df.groupby("Department")["Salary"].mean()
# print(result)



# print(df.groupby("Department").agg({"Salary":["min","max","mean","count"]}))
