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

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: введите положительное число.")
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    print("Введите размеры матрицы:")
    n = get_positive_integer("Количество строк (n): ")
    m = get_positive_integer("Количество столбцов (m): ")
    
    matrix = read_matrix(n, m)
    print_by_columns(matrix, n, m)

if __name__ == "__main__":
    main()
