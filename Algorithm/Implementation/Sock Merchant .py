n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

total = 0

while True:
    for color in c:
        if c.count(color) > 1:
            c.remove(color)
            c.remove(color)
            total += 1
            break
    else:
        break

print total
