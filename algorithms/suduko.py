N = 9
def isSafe(arr, row, col, num):
    for i in range(N):
        if arr[i][col] == num:
            return False
    for i in range(N):
        if arr[row][i] == num:
            return False
    rowMat = row - row % 3
    colMat = col - col % 3
    for i in range(rowMat, rowMat + 3):
        for j in range(colMat, colMat + 3):
            if arr[i][j] == num:
                return False
    return True

def sudoku(arr, row, col):
    if col == N and row == N - 1:
        return True
    if col == N:
        row += 1
        col = 0
    if arr[row][col] > 0:
        return sudoku(arr, row, col + 1)
    for i in range(1, N + 1):
        if isSafe(arr, row, col, i):
            arr[row][col] = i
            return sudoku(arr, row, col + 1)
    arr[row][col] = 0
    return False