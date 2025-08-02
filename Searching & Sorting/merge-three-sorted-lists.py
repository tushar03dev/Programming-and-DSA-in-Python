def merge(A, B, C):
    m,n,o = len(A),len(B),len(C)
    i = j = k = 0
    D = []
    while i < m or j < n or k < o:
        a = A[i] if i < m else float('inf')
        b = B[j] if j < n else float('inf')
        c = C[k] if k < o else float('inf')

        if a <= b and  a <= c:
            D.append(a)
            i += 1
        elif b <= c and b <= a:
            D.append(b)
            j += 1
        else:
            D.append(c)
            k += 1
    return D

if __name__ == '__main__':
 A = [1, 2, 3, 4, 5]
 B = [2, 3, 4]
 C = [4, 5, 6, 7]
 D = merge(A,B,C)
 print(D)