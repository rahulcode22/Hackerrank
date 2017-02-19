fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
print map(lambda x: x**3, map(fib, range(input())))
