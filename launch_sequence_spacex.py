from collections import defaultdict

def launchSequenceChecker(systemNames, stepNumbers):
    d = defaultdict(list)
    for n, s in zip(systemNames, stepNumbers):
        d[n].append(s)
    for k in d.keys():
        for i in range(len(d[k])-1):
            if d[k][i] >= d[k][i+1]:
                return False
    return True


names = ["stage_1", 
         "stage_1", 
          "stage_2", 
           "dragon"]

steps = [2,1,12, 111]

print(launchSequenceChecker(names, steps))

