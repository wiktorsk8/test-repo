
def power(a, N):
    if N == 0:
        return 1
    if N % 2 == 0:
        x = power(a, N//2)
        return x*x
    else:
        return a * power(a, N-1)

print(power(3,4))

print('first branch')