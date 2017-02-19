from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    item_name,item_price=input().rsplit(' ',1)
    if item_name not in d:
        d[item_name]=int(item_price)
    else:
        d[item_name]=d[item_name]+int(item_price)

for i in d.items():
    print(*i)
