def rotate_by_90(matrix, r, b, t = 0, l = 0):
    count = 0
    length = 0
    i = l
    j = r

    while i <= j:
        length += 1
        i +=1
    print(length)

    if length % 2 == 0:
        print(length, l, r)
        while count < length-1:
            print(len(matrix))
            temp = matrix[t + count][r]
            # move top to right
            matrix[t + count][r] = matrix[t][l + count]
            # move right to bottom
            temp, matrix[b][r - count] = matrix[b][r - count], temp
            # move bottom to left
            temp, matrix[b - count][l] = matrix[b - count][l], temp
            # move left to top
            temp, matrix[t][l + count] = matrix[t][l + count], temp
            count += 1
    else:
        while count <= (len(matrix)-1)//2:
            temp = matrix[t + count][r]
            # move top to right
            matrix[t + count][r] = matrix[t][l + count]
            # move right to bottom
            temp, matrix[b][r - count] = matrix[b][r - count], temp
            # move bottom to left
            temp, matrix[b - count][l] = matrix[b - count][l], temp
            # move left to top
            temp, matrix[t][l + count] = matrix[t][l + count], temp
            count += 1



    if b - t <= 2:
        for line in matrix:
            print(''.join(str(line)) + "\n")
    else:
        rotate_by_90(matrix, r - 1, b - 1, t + 1, l + 1)


matrix = [
         [1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]
         ]

matrix2 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

rotate_by_90(matrix, len(matrix)-1, len(matrix)-1)
rotate_by_90(matrix2, len(matrix2)-1, len(matrix2)-1)