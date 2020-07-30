
def arrayChange(a):
    c = 0
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            delta = a[i]-a[i+1] + 1
            a[i+1] += delta
            c += delta
    return(c)



a = [1, 1, 1]
print(arrayChange(a))
