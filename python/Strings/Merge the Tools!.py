s = raw_input()
n = int(raw_input())
j = 0
k = n

while k <= len(s):
    items = []
    for item in s[j: k]:
        if item not in items:
            items.append(item) 
    print(''.join(items))
    j = k
    k += n
