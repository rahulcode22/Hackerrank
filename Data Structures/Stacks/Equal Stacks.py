#!/bin/python

import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
sum1=sum(h1)
sum2=sum(h2)
sum3=sum(h3)
d1=0
d2=0
d3=0
while(1):
    if (d1==n1 or d2==n2 or d3==n3):
        h=0
        break
    if (sum1==sum2 and sum2==sum3):
        
        h=sum1
        break;
    #if height of stack1 is highest
    if sum1>sum2 and sum1>sum3:
        sum1=sum1-h1[d1]
        d1 +=1
    #if height of stack2 is highest
    if sum2>sum1 and sum2>sum3:
        sum2=sum2-h2[d2]
        d2 +=1
    #if height of stack3 is highest
    if sum3>sum2 and sum3>sum1:
        sum3=sum3-h3[d3]
        d3 +=1
print h
