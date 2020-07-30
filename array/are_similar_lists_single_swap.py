def areSimilar(a,b):
    idx = []
    count = 0
    for i in range(len(a)):
        if a[i] - b[i] != 0:
            idx.append(i)
            count += 1
        if count > 2:
            return False
    if count == 1:
        return False
    elif count ==2:
        return a[idx[0]] == b[idx[1]] and a[idx[1]] == b[idx[0]]
    else:
        return True

a = [1, 2, 3]
b = [1, 2, 3]
a1 = [1, 2, 3]
b1 = [2, 1, 3]
a2 = [1, 2, 2]
b2 = [2, 1, 1]
a3 = [2, 3, 1]
b3 = [1, 3, 2]

print(areSimilar2(a, b))
print(areSimilar2(a1, b1))
print(areSimilar2(a2, b2))
print(areSimilar2(a3, b3))
