def boxBlur(image):
    rn = len(image)
    cn = len(image[0])
    blurred = []
    for i in range(1, rn - 1):
        blur = []
        for j in range(1, cn - 1):
            avg = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    avg += image[i+k][j+l]
            blur.append(avg//9)
        blurred.append(blur)
    print(blurred)



image = [[7, 4, 0, 1], [5, 6, 2, 2], [6, 10, 7, 8], [1, 4, 2, 0]]


boxBlur(image)
