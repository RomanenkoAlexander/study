def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append([])
            matrix[i][j]=value
    print(matrix)

get_matrix(4,2,"13")




