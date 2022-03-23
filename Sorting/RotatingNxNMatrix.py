

def rotateImage(matrix, r):
    n = len(matrix)
    while r > 0:
        # step 1 - Transpose Matrix (turn rows to columns)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # step 2 flipping horizontally
        for i in range(n):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp
        r -= 1
    return matrix

if __name__ == '__main__':
    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]

    print(rotateImage(array, 4))