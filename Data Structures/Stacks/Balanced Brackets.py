import sys
from sys import maxsize
def createstack():
    stack=[]
    return stack
def push(stack,item):
    stack.append(item)
def isEmpty(stack):
    return len(stack)==0
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) #return minus infinite
     
    return stack.pop()
def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
     
    return stack[len(stack) - 1]

t = int(input())
for a0 in range(t):
    s = input().strip()
    n=len(s)
    st=createstack()
    for i in range(n):
        if (s[i]=='(' or s[i]=='[' or s[i]=='{'):
            push(st,s[i])
        elif (peek(st)=='(' and s[i]==')') or (peek(st)=='[' and s[i]==']') or (peek(st)=='{' and s[i]=='}'):
            pop(st)
    if isEmpty(st):
        print ("YES")
    else:
        print ("NO")
