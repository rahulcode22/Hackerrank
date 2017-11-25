input()
a = [0] + [int(x) for x in input().split()] # to make first row/col of 0's
b = [0] + [int(x) for x in input().split()]
# table will be the dynamic programming table
table = [[0 for _ in range(len(a))] for _ in range(len(b))]
# populating table
for i in range(1,len(b)):
  for j in range(1,len(a)):
    if a[j] == b[i]:
      table[i][j] = table[i-1][j-1] + 1
    else:
      table[i][j] = max(table[i][j-1], table[i-1][j])

# table[len(b)-1][len(a)-1] is the length of longest common subsequence
# in order to find the subsequence we have to trace back from that square
# see where the matches where and add them to word common_subsequence
length = table[len(b)-1][len(a)-1]
common_subsequence = []
curr = len(b)-1,len(a)-1 # save my current index in table in the search
while length:
  if b[curr[0]] == a[curr[1]]: # match - belongs to common subseq
    common_subsequence.append(b[curr[0]])
    length -= 1
    curr = (curr[0]-1,curr[1]-1)
  else: # go to the square that has longer subsequence until now
    if table[curr[0]-1][curr[1]] > table[curr[0]][curr[1]-1]:
      curr = (curr[0]-1,curr[1])
    else:
      curr = (curr[0],curr[1]-1)

print(' '.join(str(x) for x in common_subsequence[::-1])) # reverse
