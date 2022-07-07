#/bin/pyhton3.10

'''
Write a python program to perform basic matrix operations on user entered matrices.
'''

def row_column():
    while True:
        try:
            try:
                row = int(input("Enter the number of rows of the matrix : "))
                column = int(input("Enter the number of colnumns of the matrix : "))
                if row >= 1 and column >= 1:
                    break
                else:
                    print("Enter number more than or equal to 1 for rows/column")
            except Exception as e:
                print("Enter only integer value for row/column")
        except KeyboardInterrupt:
            print("Invalid Key Binding")
    return row,column

def choice_fun():
    print('''The available functions are :\n
          1) Addition
          2) Subtraction
          3) Multiplication
          4) Transpose
          5) Exit''')
    while True:
        try:
            try:
                choice = int(input("Choice : "))
                if choice <= 5 and choice > 0:
                    break
                else:
                    print("Enter from above choice only")
            except Exception as e:
                print("Invalid Input")
        except KeyboardInterrupt:
            print("Invalid Key Binding")
    return choice

def matrix_addition(matrix1,matrix2):
    sum_matrix = []
    for row_val in range(len(matrix1)):
        lst = []
        for col_val in range(len(matrix1[0])):
            lst.append(matrix1[row_val][col_val] + matrix2[row_val][col_val])
        sum_matrix.append(lst)
    return sum_matrix

def matrix_subtraction(matrix1,matrix2):
    sum_matrix = []
    for row_val in range(len(matrix1)):
        lst = []
        for col_val in range(len(matrix1[0])):
            lst.append(matrix1[row_val][col_val] - matrix2[row_val][col_val])
        sum_matrix.append(lst)
    return sum_matrix
    
def matrix_multiplication(matrix1,matrix2):
    if len(matrix1[0]) == len(matrix2):
        product_matrix = []
        for col in range(len(matrix1[0])):
            lst = []
            for row in range(len(matrix1)):
                lst.append(0)
            product_matrix.append(lst)
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    product_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return product_matrix
    else:
        print("The Multiplication is not possible\nas the number of columns of matrix 1\nis not equal to number of rows or matrix 2.")
        main()

def matrix_transpose(matrix):
    transpose_matrix = []
    for i in range(len(matrix[0])):
        lst = []
        for j in range(len(matrix)):
            lst.append(matrix[j][i])
        transpose_matrix.append(lst)
    return transpose_matrix

def input_matrix(row,column):
    lst2 = []
    for row_val in range(row):
        lst = []
        for col_val in range(column):
            while True:
                try:
                    try:
                        lst.append(int(input("Enter : ")))
                        break
                    except Exception as e:
                        print("\nEnter only integer value \n")
                except KeyboardInterrupt:
                    print("Invalid Key Binding")
        lst2.append(lst)
    return lst2

def main():
    choice = choice_fun()
    
    if choice == 1:
        print("Enter the values of the matrixfirst {0} will be the element of the rows")
        print("Matrix 1")
        row_col = row_column()
        matrix1 = input_matrix(row_col[0],row_col[1])
        print("Matrix 2")
        row_col = row_column()
        matrix2 = input_matrix(row_col[0],row_col[1])
        sum_matrix = matrix_addition(matrix1,matrix2)
        for row in range(len(sum_matrix)):
            print(sum_matrix[row])
        main()
            
    elif choice == 2:
        print("Enter the values of the matrixfirst {0} will be the element of the rows")
        print("Matrix 1")
        row_col = row_column()
        matrix1 = input_matrix(row_col[0],row_col[1])
        print("Matrix 2")
        row_col = row_column()
        matrix2 = input_matrix(row_col[0],row_col[1])
        diff_matrix = matrix_subtraction(matrix1,matrix2)
        for row in range(len(diff_matrix)):
            print(diff_matrix[row])
        main()
        
    elif choice == 3:
        print("Enter the values of the matrixfirst {0} will be the element of the rows")
        print("Matrix 1")
        row_col = row_column()
        matrix1 = input_matrix(row_col[0],row_col[1])
        print("Matrix 2")
        row_col = row_column()
        matrix2 = input_matrix(row_col[0],row_col[1])
        product_matrix = matrix_multiplication(matrix1,matrix2)
        for row in range(len(product_matrix)):
            print(product_matrix[row])
        main()
    
    elif choice == 4:
        print("Enter the values of the matrixfirst {0} will be the element of the rows")
        row_col = row_column()
        print("Matrix")
        matrix = input_matrix(row_col[0],row_col[1])
        transpose_matrix = matrix_transpose(matrix)
        for row in range(len(transpose_matrix)):
                print(transpose_matrix[row])
        main()

    else:
        print("Thank You for using the program... \nSee you later\nExiting.......")
        exit()
        
main()