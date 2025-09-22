r = int(input())

def is_Prime(value):

    prime = True

    for i in range(2, int(value**0.5)+1):
        if not(value % i):
            prime = False
            break
        
    return prime
    
for k in range(2, int(r/2)+1):
    if not(r % k):
        if is_Prime(r // k):
            print(r // k)
            break
