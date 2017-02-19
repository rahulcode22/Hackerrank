n = int(input())

mystring = ""
history = []

for i in range(n):
    myinput = input().strip().split(' ')
    
    if myinput[0] == '1':
        history.append(mystring)
        mystring = mystring + myinput[1]
    elif myinput[0] == '2':
        history.append(mystring)
        delpos = int(myinput[1])
        mypos = len(mystring) - delpos
        mystring = mystring[0:mypos]
    elif myinput[0] == '3':
        mypos = int(myinput[1]) - 1
        print(mystring[mypos])
    else:
        mystring = history.pop()
