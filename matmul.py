r1 = int(input("Rows for matrix A: "))
c1 = int(input("Cols for matrix A: "))
r2 = int(input("Rows for matrix B: "))
c2 = int(input("Cols for matrix B: "))

if c1 != r2:
    print("Cannot multiply!")
else:
    A = []
    B = []
    
    print("Matrix A:")
    for i in range(r1):
        r = []
        for j in range(c1):
            v = int(input(f"A[{i}][{j}]: "))
            r.append(v)
        A.append(r)
    
    print("Matrix B:")
    for i in range(r2):
        r = []
        for j in range(c2):
            v = int(input(f"B[{i}][{j}]: "))
            r.append(v)
        B.append(r)
    
    C = []
    for i in range(r1):
        row = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += A[i][k] * B[k][j]
            row.append(s)
        C.append(row)
    
    print("Result:")
    for i in range(r1):
        for j in range(c2):
            print(C[i][j], end=" ")
        print()