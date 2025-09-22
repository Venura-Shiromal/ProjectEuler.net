def is_Mirrored(n):
    original_list = []
    reversed_list = []
    
    for x in range(len(str(n))):
        original_list.append(str(n)[x])
        reversed_list.append(str(n)[x])

    reversed_list.reverse()

    if original_list == reversed_list:
        return True
    else:
        return False

multi = []
mirrors = []

for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        multi.append(i*j)

for num in multi:
    if is_Mirrored(num):
        mirrors.append(num)

print(max(mirrors))
