import numpy
N, M = map(int, raw_input().split())
A = numpy.array([raw_input().split() for _ in range(N)],int)
print numpy.mean(A,axis=1)
print numpy.var(A,axis=0)
print numpy.std(A)
