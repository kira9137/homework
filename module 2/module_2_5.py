def get_matrix(n, m, value):
  matrix = []
  for i in range(n):
      row = []
      for j in range(m):
          row.append(value)
      matrix.append(row)
  return matrix

print('Матрица:', get_matrix(2, 3, 'o'))
