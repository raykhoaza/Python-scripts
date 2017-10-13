from dfs import dfs
#pad the adjacency matrix with extra O's at top, bottom, and both sides
#to compensate for out of range index while doing dfs, only matters when
#see X's in the matrix
def pad_matrix(matrix, n, m):
    for each in matrix:
        each.append('O')
        each.insert(0, 'O')

    extra_line = []
    for i in range(0, m+2):
        extra_line.append('O')

    matrix.insert(0, extra_line)
    matrix.append(extra_line)
#This program runs to find the total shapes inside a text file, counting only
#adjacent X's as shapes, using depth first search
def main():
    #colums and rows of adjacency matrix
    n = 10
    m = 3
    #actual text of the matrix
    line = 'XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO'

    shapes = 0
    matrix = []
    #parsing the text into a nested list to represent the matrix
    line_splitted = line.split(' ')

    for word in line_splitted:
        matrix.append(list(word))

    #code to compensate for out of bond indexes
    pad_matrix(matrix, n, m)

    #print(matrix)
    #use n+2 and m+2 to compensate for the padded O's on the matrix
    for i in range(0, n+2):
        for j in range(0, m+2):
            #run dfs everytime there is an X and then return after finding
            #all adjacent X's
            if matrix[i][j] == 'X':
                dfs(matrix, i, j)
                shapes+=1

    print(shapes)

if __name__ == "__main__":
    main()
