#  Double Matrix
import sys

n, m = map(int, raw_input().split())

matrix1 = []
matrix2 = []
for i in range(n):
    matrix1.append(map(int, raw_input().split()))
for i in range(n):
    matrix2.append(map(int, raw_input().split()))

possible = True

for i in range(n):
    for j in range(m):
        if j < m - 1 and (matrix1[i][j] >= matrix1[i][j + 1] or matrix2[i][j] >= matrix2[i][j + 1]):
            if matrix1[i][j] < matrix2[i][j + 1] and matrix2[i][j] < matrix1[i][j + 1]:
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
            else:
                possible = False

for j in range(m):
    for i in range(n):
        if i < n - 1 and (matrix1[i][j] >= matrix1[i + 1][j] or matrix2[i][j] >= matrix2[i + 1][j]):
            if matrix1[i][j] < matrix2[i + 1][j] and matrix2[i][j] < matrix1[i + 1][j]:
                matrix1[i][j], matrix2[i][j] = matrix2[i][j], matrix1[i][j]
            else:
                possible = False

print "Possible" if possible else "Impossible"