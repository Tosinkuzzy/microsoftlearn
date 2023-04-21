# Defining base case
f0 = 0
f1 = 1
# Then we calculate
f2 = f1 + f0
f2
f3 = f2 + f1
f3
f4 = f3 + f2
f4
# Principles of recursion
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
# count
fib(5)
fib(6)
fib(10)