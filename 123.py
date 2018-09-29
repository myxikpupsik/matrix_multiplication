A = []
a = []
B = []
b = []
print("Enter the size of matrix 1")
size_of_matrix_1r = int(input())
size_of_matrix_1c = int(input())
print("Enter the size of the matrix 2")
size_of_matrix_2r = int(input())
size_of_matrix_2c = int(input())
if size_of_matrix_1c != size_of_matrix_2r:
    print("multiplication cannot be done")
print("Enter elements of the matrix from first row")
try:
    while len(a) != size_of_matrix_1c:
        for i in range(size_of_matrix_1r):
            a = [int(x) for x in input().split()]
            if len(a) != size_of_matrix_1c:
                print("You entered bad data, please try again")
            A.append(a)
except IndexError:
    pass
print("Enter elements of the matrix B")
try:
    while len(b) != size_of_matrix_2c:
        for i in range(size_of_matrix_2r):
            b = [int(x) for x in input().split()]
            if len(b) != size_of_matrix_2c:
                print("You entered bad data, please try again")
            B.append(b)
except IndexError:
    pass
result = [[0 for x in range(size_of_matrix_2c)] for l in range(size_of_matrix_1r)]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            try:
                result[i][j] += A[i][k]*B[k][j]
            except IndexError:
                pass
print(result)


