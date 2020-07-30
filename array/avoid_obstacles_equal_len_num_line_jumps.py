
def avoidObstacles(a):
    distance = max(a) + 2
    for j in range(1, distance):
        i = j
        while i not in a:
            if i > distance:
                return j
            i += j







a = [2,3]

print(avoidObstacles(a))
