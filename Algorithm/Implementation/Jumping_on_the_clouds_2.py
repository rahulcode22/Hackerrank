n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

ind, jump = 0, 0
while ind < n - 1:
    if c[ind] == 1:
        ind -= 1
    jump += 1
    ind = ind + 2
    
print jump
