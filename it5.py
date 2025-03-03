def numm(a):
    for i in range(a,-1,-1):
            yield i
a=int(input())
for i in numm(a):
    print(i)