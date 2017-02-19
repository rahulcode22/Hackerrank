import re
t=int(raw_input())
for i in range(t):
    s=raw_input()
    try:
        re.compile(s)
        is_valid = True
    except re.error:
        is_valid = False
    print is_valid
