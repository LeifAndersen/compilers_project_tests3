x = [[1],[2],[3],[4,5,6]]
for i in x:
 for j in i:
  print(j)
i = 0
for k in x:
 j = 0
 for m in k:
  print(x[i][j])
  j += 1
 i = i + 1

