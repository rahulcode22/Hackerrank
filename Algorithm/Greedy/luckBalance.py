n, k = map(int,raw_input().split())
impt = []
impt_sum = 0
unimpt_sum = 0
for i in range(n):
    l ,t = raw_input().split()
    l, t = [int(l), int(t)]
    if t:
        impt.append(l)
        impt_sum += l
    else:
        unimpt_sum += l
impt = sorted(impt)
if k <= len(impt):
    for i in range(0,len(impt)-k):
        impt_sum -= 2*impt[i]
        #print
print impt_sum + unimpt_sum
