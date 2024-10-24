class Matrix:
    
    def __init__(self, rows, columns, values):

        self.rows = rows
        self.columns = columns
        self.matrix = [values[i*columns:(i+1)*columns] for i in range(rows)]
        

    def addition(self, matrix_2):

        if self.rows != matrix_2.rows or self.columns != matrix_2.columns:
            raise ValueError('Матриці різних розмірів')

        for row in range(self.rows):
            for column in range(self.columns):
                self.matrix[row][column] = self.matrix[row][column] + matrix_2.matrix[row][column]

        
    def subtraction(self, matrix_2):

        if self.rows != matrix_2.rows or self.columns != matrix_2.columns:
            raise ValueError('Матриці різних розмірів')

        for row in range(self.rows):
            for column in range(self.columns):
                self.matrix[row][column] = self.matrix[row][column] - matrix_2.matrix[row][column]

                

    def multiplication(self, matrix_2):

        if self.columns != matrix_2.rows:
            raise ValueError('Кількість стовпців першої матриці не дорівнює кількості рядків другої')

        result_matrix = [[0 for _ in range(matrix_2.columns)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(matrix_2.columns):
                for k in range(self.columns):
                    result_matrix[i][j] += self.matrix[i][k] * matrix_2.matrix[k][j]

        self.matrix = result_matrix


M = Matrix(1, 2, [2, 3, 1, 4])
M2 = Matrix(1, 2, [5, 1, 0, 3])
print(M2.matrix)
M.addition(M2)
print(M.matrix)
