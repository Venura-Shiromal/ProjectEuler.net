def is_Prime(value):

    prime = True

    for i in range(2, int(value**0.5)+1):
        if not(value % i):
            prime = False
            break
        
    return prime

primes = []

for j in range(2,2000000):
    if is_Prime(j):
        primes.append(j)

print(sum(primes))
