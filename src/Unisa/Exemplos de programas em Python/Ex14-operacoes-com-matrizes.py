print 'Considere as matrizes [[4,5], [3,2]] e [[2,1], [1,6]] :'
matriz = [[4, 5], [3, 2]]
matriz1 = [[2,1], [1,6]]
diagonal_principal = [matriz[i][i] for i in (0,1)]
diagonal_principal_1 = [matriz1[j][j] for j in (0,1)]
print 'Diagonal principal da matriz [[4,5], [3,2]] = ', diagonal_principal
print 'Diagonal principal da matriz [[2,1], [1,6]] = ', diagonal_principal_1
c = [matriz[0][0] + matriz1[0][0], matriz[0][1] + matriz1[0][1]], [matriz[1][0] + matriz1[1][0], matriz[1][1] + matriz1[1][1]] 
print 'Soma das matrizes = ', c
a = [matriz[0][0] - matriz1[0][0], matriz[0][1] - matriz1[0][1]], [matriz[1][0] - matriz1[1][0], matriz[1][1] - matriz1[1][1]] 
print 'Subtracao das matrizes = ', a
b = [(matriz[0][0] * matriz1[0][0] + matriz[0][1] * matriz1[1][0]), (matriz[0][0] * matriz1[0][1] + matriz[0][1] * matriz1[1][1])], [(matriz[1][0] * matriz1[0][0] + matriz[1][1] * matriz1[1][0]), (matriz[1][0] * matriz1[0][1] + matriz[1][1] * matriz1[1][1])]
print 'Multiplicacao das matrizes = ', b
