# Transpose of matrix using list comprehension
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for r in result:
    print(r)
