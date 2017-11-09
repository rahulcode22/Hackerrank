string = raw_input()
oddcount=0
found = False
set1 = set(string)
for val in set1:
    if string.count(val) % 2 == 0:
        next
    else:
        oddcount+=1
if oddcount > 1:
    found = False
else:
    found = True
if not found:
    print("NO")
else:
    print("YES")
