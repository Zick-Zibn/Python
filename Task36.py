def print_operation_table(operation, num_rows, num_columns):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

num_rows = int(input("Введите количество строк: "))
num_columns = int(input("Введите количество столбцов: "))

print_operation_table(lambda x, y: x * y, num_rows, num_columns)