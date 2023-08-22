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
