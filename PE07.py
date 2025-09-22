def is_Prime(value):

    prime = True

    for i in range(2, int(value**0.5)+1):
        if not(value % i):
            prime = False
            break
        
    return prime

primes = []
n = 2

while len(primes) <= 10001:
    if is_Prime(n):
        primes.append(n)
    n += 1

print(primes[10000])
