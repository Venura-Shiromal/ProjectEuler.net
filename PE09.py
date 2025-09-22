def is_Trio(a,b):
    
    trio = False

    c = (a**2 + b**2)**0.5

    if c ==  int(c):
        trio = True

    return trio

trios = []

for a in range(1, 1000):
    for b in range(1, 1000):

        abc = []

        if is_Trio(a, b):
            abc.append(a)
            abc.append(b)
            abc.append(int((a**2 + b**2)**0.5))

            trios.append(abc)

for sublist in trios:
    if sum(sublist) == 1000:
        print(sublist[0]*sublist[1]*sublist[2])
    
