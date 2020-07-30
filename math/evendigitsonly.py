def evenDigitsOnly(n):
        return all([int(i)%2==0 for i in str(n)])

n = 2348972
n1 = 248626

print(evenDigitsOnly(n))
print(evenDigitsOnly(n1))
    
