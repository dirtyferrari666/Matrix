def read_matrix(n, m):
    matrix = []
    print("Введите матрицу построчно, элементы разделяйте пробелами:")
    for i in range(n):
        row = list(map(float, input(f"Строка {i+1}: ").split()))
        while len(row) != m:
            print("Ошибка: количество элементов не соответствует m.")
            row = list(map(float, input(f"Строка {i+1}: ").split()))
        matrix.append(row)
    return matrix

def print_by_columns(matrix, n, m):
    print("\nМатрица, выведенная по столбцам:\n")
    for col in range(m):
        print(f"Столбец {col + 1}:")
        for row in range(n):
            print(matrix[row][col])
        print()

def main():
    print("Введите размеры матрицы:")
    n = int(input("Количество строк (n): "))
    m = int(input("Количество столбцов (m): "))
    matrix = read_matrix(n, m)
    print_by_columns(matrix, n, m)

if __name__ == "__main__":
    main()