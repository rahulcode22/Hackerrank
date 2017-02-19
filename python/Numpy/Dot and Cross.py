
import numpy as np
n=int(input().strip())
a=np.array([list(map(int,input().split())) for _ in range(n)])
b=np.array([list(map(int,input().split())) for _ in range(n)])
print(np.dot(a,b))
