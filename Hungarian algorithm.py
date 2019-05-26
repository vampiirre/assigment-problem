import numpy as np

n = int(input('Input number of rows in matrix '))
Z = np.zeros((n*n), dtype=int).reshape(n, n)
for i in range(n*n):
    Z[i//n, i%n] = int(input('Input elem in ' + str(i//n) + ' row and ' + str(i%n) + ' coloumn '))
for i in range(n):
    Z[i,:] -= Z[i,:].min()
    Z[:,i] -= Z[:,i].min()
I = np.zeros((n), dtype=int)
I -= 1
while(I.min() == -1):
    i = 0
    j = 0
    J = np.zeros((n), dtype=int)
    J -= 1
    I = np.zeros((n), dtype=int)
    I -= 1
    while (i < n):
        while(i < n) & (j < n):
            if ((Z[i,j] + J[j] + 1) == 0):
                I[i] = j
                J[j] = i
                i += 1
                j = 0
            else:
                j += 1
        i += 1
        j = 0
    k = 1
    while(k == 1):
        k = 0
        for i in range(n):
            if(I[i] == -1):
                for j in range(n):
                    if(Z[i, j] == 0):
                        for j2 in range(n):
                            if((Z[J[j], j2] == 0) and (J[j2] == -1)):
                                k = 1
                                I[i] = j
                                J[j2] = J[j]
                                I[J[j]] = j2
                                J[j] = i
    if(I.min() == -1):
        I2 = np.ones((n), dtype=int)
        J2 = np.zeros((n), dtype=int)
        I2[I == -1] = 0
        k = 1
        while(k == 1):
            k = 0
            for i in range(n):
                if(I2[i] == 0):
                    for j in range(n):
                        if ((J2[j] == 0) and (Z[i, j] == 0) and (I[i] != j)):
                            J2[j] = 1
                            k = 1
            for j in range(n):
                if(J2[j] == 1):
                    for i in range(n):
                        if ((I2[i] == 1) and (Z[i, j] == 0) and (J[j] == i)):
                            I2[i] = 0
                            k = 1
        m = Z[:,J2 == 0][I2 == 0, :].min()
        Z -= m
        Z[:,J2 == 1] += m
        Z[I2 == 1,:] += m
Answer = np.zeros((n*n), dtype=int).reshape(n, n)
print('Matrix of selected elements:')
for el, i in enumerate(I):
    Answer[el][i] = 1
print(Answer)
