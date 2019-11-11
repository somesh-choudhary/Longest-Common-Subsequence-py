def lcs(st1, st2):
    s =""
    import re
    import numpy as np

    list1 = []
    sr1 = re.sub('[^A-Za-z0-9]+','',st1)
    sr2 = re.sub('[^A-Za-z0-9]+','',st2)
    n1 = len(st2)
    n2 = len(st1)
    table = np.zeros((n1 + 1, n2 + 1))
    dir = np.zeros((n1 + 1, n2 + 1))
    
    for i in range (1, n1 + 1):
        for j in range (1, n2 + 1):
            if st2[i - 1] == st1[j - 1]:
                dir[i][j] = 1
                table[i][j] = table[i - 1][j - 1] + 1
            elif table[i][j - 1] > table[i - 1][j]:
                dir[i][j] = 2
                table[i][j] = table[i][j - 1]
            else:
                dir[i][j] = 3
                table[i][j] = table[i - 1][j]

    k = table[n1][n2]
    k = k - 1
    i = n1
    j = n2
    k = int(k)
    print(k)
    index = np.array([0] * (k+1))

    while k >= 0:
        if dir[i][j] == 1:
            index[k] = j - 1
            k = k - 1
            j = j - 1
            i = i - 1

        elif dir[i][j] == 2:
            j = j - 1
        else:
            i = i - 1

    k = table[n1][n2]
    for i in range(int(k)):
        list1.append(st1[index[i]])

    for x in list1:
        s += x
    return s
