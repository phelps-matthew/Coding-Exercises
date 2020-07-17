def mysum(s):
    if len(s) < 1:
        return 0
    else:
        end = s[-1]
        return mysum(s[:-1]) + end

def matrix_comp(n):
    count = 0
    for b in range(1, n):
        for i in range(n-b):
            j = i + b
            print("i={}, j={}".format(i,j))
            for k in range(i,j):
                print(k,end=',')
                count += 1
            print("\n")
        input("Press return to continue")
    return count

if __name__ == "__main__":
    print(matrix_comp(10))

