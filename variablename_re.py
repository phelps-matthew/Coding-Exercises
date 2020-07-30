import re

def variableName(name):
    find = re.fullmatch("^([a-zA-Z]|_)+(\w|_)*$", name)
    return bool(find)



name = "var_1__Int"
name1 = "var[riable0"
name2 = "2w2"
#print(variableName(name))
print(variableName(name1))
#print(variableName(name2))
