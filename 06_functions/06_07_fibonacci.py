def fib1 (n):
    i = 1
    j = 1
    if n >= 1:
        yield i
    if n >= 2:
        yield j
    
    k = 2
    while k < n:
        next_number = i + j
        yield next_number
        i = j
        j = next_number
        k += 1

print([x for x in fib1(10)])

# recursive:
# F(10) = F(9) + F(8)
def fib2(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return fib2(n-1) + fib2(n-2)

print(fib2(10))
print([fib2(x) for x in range(1, 11)])

