#Implementation for DFS using an adjacency matrix filled with X and O
def dfs(matrix, n, m):
    matrix[n][m] = 'O'
    if matrix[n][m-1] == 'X':
        dfs(matrix, n, m-1)
    if matrix[n][m+1] == 'X':
        dfs(matrix, n, m+1)
    if matrix[n-1][m] == 'X':
        dfs(matrix, n-1, m)
    if matrix[n+1][m] == 'X':
        dfs(matrix, n+1, m)
