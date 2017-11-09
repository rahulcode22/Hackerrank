import re
from itertools import combinations
s_len = int(raw_input().strip())
string = raw_input().strip()
setS = list(set(string))
nominated = []
selections = list(map("".join, (combinations(setS, r=2))))
for i in selections:
    reg = re.sub(r"[^"+i+"]", r"", string)
    if len(reg) < 2:
        continue
    flag = True
    for j in range(len(reg)):
        if j%2==0:
            if reg[0] != reg[j]:
                flag = False
                break
        else:
            if reg[1] != reg[j]:
                flag = False
                break
    if flag:
        nominated.append(reg)

print (max(map(len, nominated)) if nominated else 0)
