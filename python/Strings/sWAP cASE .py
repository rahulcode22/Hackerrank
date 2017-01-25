S = raw_input()

swapped = ""

for c in S:
    if c.islower():
        swapped+=c.upper()
    elif c.isupper():
        swapped+=c.lower()
    else:
        swapped+=c

print swapped
