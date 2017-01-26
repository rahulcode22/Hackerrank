
import string
a = int(input())
width = (4*(a-1)+1)
alphabet = string.ascii_lowercase
for i in range(a-1,-a,-1):
    l = [alphabet[j] for j in range(a-1,abs(i)-1,-1)]
    l.extend([alphabet[j] for j in range(abs(i)+1,a)])
    print ('-'.join(l).center(width,'-'))
