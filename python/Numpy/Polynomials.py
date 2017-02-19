import numpy as np
coeff = np.array(raw_input().split(" "), float)
x = map(float, raw_input())
print np.polyval(coeff,x)[0]
