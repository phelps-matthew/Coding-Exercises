def addBorder(picture):
    n = len(picture[0])
    pic = ["*" * n] + ["*" + row + "*" for row in picture] + ["*" * n]
    return pic


picture = ["abc", "ded"]

print(addBorder(picture))
