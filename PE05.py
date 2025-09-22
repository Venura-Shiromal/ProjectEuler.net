n = 232792560
con = True

while con:
    
    con1 = True

    for i in range(1,21):
        if not(n % i == 0):
            con1 = False
            break
    
    if con1:
        print(n)
        con = False
    else:
        n += 1
