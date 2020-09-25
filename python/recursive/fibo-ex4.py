import time

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else: return fibo(n-1) + fibo(n-2)
start = time.time()

def fibo_it(i):
    a, b, cpt = 0,1,0
    while cpt <= i:
        if cpt < 2:
            c = cpt
        else:
            c = a+b
            a=b
            b=c
        cpt+=1
    return c

print(fibo_it(500))

#print(fibo(41))
#end = time.time()
#print(end - start)
