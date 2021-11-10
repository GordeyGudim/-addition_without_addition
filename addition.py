def power(a, n):
    if n ==  0:
        return a
    if n != 0:
        return power(a+1, n-1)
a = int(input())
n =  int(input())
print(power(a, n))