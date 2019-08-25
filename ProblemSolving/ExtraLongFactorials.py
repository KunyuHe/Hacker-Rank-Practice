def factor(n):
    if n == 1:
        return n
    return n * factor(n-1)

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    print(factor(n))