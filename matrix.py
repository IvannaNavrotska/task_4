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


    def LUP_decomposition(self):
        
        if self.rows != self.columns:
            raise ValueError('Матриця має бути квадратною для LUP-розкладу')

        n = self.rows
        P = list(range(n))
        
        #крок 2 і 3
        for k in range(n):
            max_index = k
            max_value = abs(self.matrix[k][k])
            for i in range(k + 1, n):
                if abs(self.matrix[i][k]) > max_value:
                    max_value = abs(self.matrix[i][k])
                    max_index = i
                    
            # крок 4
            if self.matrix[max_index][k] == 0: 
                raise ValueError('Матриця є виродженою, розклад неможливий')
        
            # кроки 5 та 6
            if max_index != k: 
                self.matrix[k], self.matrix[max_index] = self.matrix[max_index], self.matrix[k]
                P[k], P[max_index] = P[max_index], P[k]
                
            # крок 7
            for i in range(k + 1, n):
                self.matrix[i][k] /= self.matrix[k][k] # крок 8
                
                # кроки 9 та 10
                for j in range(k + 1, n):
                    self.matrix[i][j] -= self.matrix[i][k] * self.matrix[k][j]
        
        L = [[0] * n for _ in range(n)]
        U = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    L[i][j] = 1  
                if i <= j:
                    U[i][j] = self.matrix[i][j]  
                else:
                    L[i][j] = self.matrix[i][j]  

        return P, L, U






M = Matrix(4, 4, [-1, 2, 3, 8, 1, 7, 3, -4, -1, 1, 4, -1 ,2, -4, -1, 6])
for row in M.matrix:
    print(row)

P = M.LUP_decomposition()
for row in M.matrix:
    print(row)

print(P)

