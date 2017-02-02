#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
max=-999
for i in range(0,4):
    for j in range(0,4):
        sum=0
        sum =sum+arr[i][j]+arr[i][j+1]+arr[i][j+2]
        sum =sum+arr[i+1][j+2]
        sum =sum+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if (sum>max):
            max=sum
print max
        
    
