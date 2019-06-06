n, m, k = map(int, raw_input().split())
operations = []
rowOp = {}
colOp = {}
for i in range(k):
    op = raw_input().split()
    if op[0] == "1":
        if op[1] in rowOp:
            operations[rowOp[op[1]]] = None
        rowOp[op[1]] = i
        operations.append(op)
    else:
        if op[1] in colOp: 
            operations[colOp[op[1]]] = None
        colOp[op[1]] = i
        operations.append(op)
matrix = [["0" for i in range(m)] for j in range(n)]

for operation in operations:
    if operation != None:
        if operation[0] == "1":
            i = int(operation[1]) - 1
            color = operation[2]
            for j in range(len(matrix[i])):
                matrix[i][j] = color
        else:
            j = int(operation[1]) - 1
            color = operation[2]
            for i in range(len(matrix)):
                matrix[i][j] = color

output = [" ".join(row) for row in matrix]
output = "\n".join(output)
print output