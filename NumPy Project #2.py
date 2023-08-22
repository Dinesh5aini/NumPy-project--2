import csv
import numpy as np

data=[]

with open(r"D:\downloads\MER_T07_02A-2020-02-03.csv",'r') as csvfile:
    file_reader = csv.reader(csvfile,delimiter=',')
    for row in file_reader:
        data.append(row)

data=np.array(data)

'''
1. Explore the important attributes like dimension,shape, data type etc, of the array formed
above.
'''

print("Dimension of array:",np.ndim(data))
print("Shape:",np.shape(data))
print("Data type:",type(data))

print()

'''
2. Print the data contained in the first 10 rows of the 4th column.
'''
data_10row_4thCol=data[1:11,3]
print("Data contained in the first 10 rows of 4th column:\n",data_10row_4thCol)

print()

'''
3. Which row serves as the headers/titles for all the columns.
'''
print(f"Row 1 serves as the header for all the columns.\n",data[0,:])

print()

'''
4. Print the data contained in column 2 and 3 from row 1 till row 20
'''
print("The data contained in column 2 and 3 from row 1 till row 20 is:\n",data[1:21,1:3])

print()

'''
5. Print the data present in only the first three and the last three rows of all the columns in a
single output.
'''
data_F_L_3row=np.concatenate((data[1:4,:], data[-3:,:]),axis=0)
print("the data present in only the first three and the last three rows of all the columns:\n",data_F_L_3row)

print()

'''
6. Sort the data on the basis of net amount of electricity generated irrespective of the
source.
'''


print()

'''
7. Find the total amount of electricity generated using coal and nuclear between
1949-1990.( In this dataset, rows containing monthly data express date in the format
'YYYYMM'. Rows containing annual data express the date in the format 'YYYY13'.)
'''

print()

'''
8. Print all the unique sources of Energy generation present in the dataset
'''
print("The unique sources of Energy generation:\n",np.unique(data[:,0:1]))

print()

