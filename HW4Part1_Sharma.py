# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 13:20:25 2025

@author: vishs
"""

# Importing pandas to read the input file
import pandas as pd

# Reading the input file 
array=pd.read_csv('C:/PCDA/2021/Data/input.txt',header=None).values
array

# Saving the first number to compare it with the nextones
prev_number=array[0]

# Variable to save how many increases there are
count=0

# For loop to compare each of the numbers in the input
for i in range (1, len (array)):
    if array[i]>prev_number:
        count+=1
    prev_number=array[i]

print(f"The number of times a depth measurement increases: {count}")

prev_window=array[0]+array[1]+array[2]

# Variable to save how many increases there are
count=0

# For loop to compare each of the sum of numbers in the input
for i in range (1, len (array)):
    
    if i+2 < len(array):
        new_window=array[i]+array[i+1]+array[i+2]
    else:
        break
    if new_window>prev_window:
        count+=1
    prev_window=new_window    
print(f"The number of times the sum of a 3-measurement window increases is: {count}")