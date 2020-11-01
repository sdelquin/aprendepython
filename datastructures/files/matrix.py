A = [[6, 4, 2], [8, 9, 1]]
B = [[3, 2], [1, 7], [9, 6]]

output_num_rows = len(A)
intermatrix_count = len(B)  # = len(A[0])
output_num_cols = len(B[0])

P = []
for i in range(output_num_rows):
    row = []
    for j in range(output_num_cols):
        result = 0
        for k in range(intermatrix_count):
            result += A[i][k] * B[k][j]
        row.append(result)
    P.append(row)

print(P)
