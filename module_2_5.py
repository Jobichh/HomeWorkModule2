def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input("Количество строк матрица: "))
m = int(input("Количество столбцов матрицы: "))
value = input("Значение матрицы: ")
matrix = get_matrix(n, m, value)\

if n <= 0:
    print("Неверное кол-во строк")
elif m <= 0:
    print("Неверное кол-во столбцов")
else:
    print("Матрица")
    for i in matrix:
        print(*i)