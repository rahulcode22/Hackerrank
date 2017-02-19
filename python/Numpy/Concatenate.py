import numpy
n,m,p=map(int,raw_input().split())
array1 = numpy.array([raw_input().strip().split() for _ in range(n)], int)
array2 = numpy.array([raw_input().strip().split() for _ in range(m)], int)
print numpy.concatenate((array1,array2),axis=0)
