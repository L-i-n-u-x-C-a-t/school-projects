m = ["a", "b", "c", "d", "e", "f", "g"]
table= [[0,1,1,1,0,0,0],
    [1,0,0,0,1,1,1],
    [1,0,0,0,0,0,0],
    [1,0,0,0,0,0,1],
    [0,1,0,0,0,1,0],
    [0,1,0,0,1,0,0],
    [0,1,0,1,0,0,0]]

txt=""
for i in range(len(table)):
    txt = m[i]+"-->"
    for j in range(len(table[i])):
        if table[i][j]==1:
            txt+=m[j]
    print(txt)
