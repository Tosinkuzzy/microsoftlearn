# The First rule of recursion
def count(n):
    return n + count(n - 1)
# Base case which will not call itself anymore
def count(n):
    if n == 0:
        return 0
    return n + count(n - 1)
# we call it
count(6)


