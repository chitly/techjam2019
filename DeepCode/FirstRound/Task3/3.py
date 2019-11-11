# A = int(input())
# table1 = list()
# table1.append(list())
# table1[0].append(0)
# for i in range(1, A + 1):
#     tmp = int(input())
#     table1.append(list())
#     table1[i].append(tmp)
# B = int(input())
# for i in range(0, A):
#   if i == 0:
#     for j in range(0, B):
#       table1[i].append(int(input()))
#   else:
#     for j in range(1, B + 1):
#       table1[i].append(table1[i][0] + table1[i-1][j])

# for i in range(0, A + 1):
#   for j in range(0, B + 1):
#     print(str(table1[i][j]) + ' ', end = '')
#   print()

A = int(input())
table1 = list()
# table1[0].append(0)
for i in range(1, A + 1):
    table1.append(int(input()))
B = int(input())
line = list()
line2 = list()
line2.append(1)
line.append(table1[0])
for i in range(1, B + 1):
  tmp = int(input())
  line.append(line[i-1]+tmp)

for i in range(1, A):
  for j in line:
    print(j, end = ' ')
  print()
  line[0] = table1[i]
  for j in line:
    print(j, end = ' ')
  print()
  for j in range(1, B + 1):
    line[j] = line[0] + line[j]
    print(str(line[j]) + ' ', end='')
  print()

  

# for i in range(0, A):
#   if i == 0:
#     for j in range(0, B):
#       table1[i].append(int(input()))
#   else:
#     for j in range(1, B + 1):
#       table1[i].append(table1[i][0] + table1[i-1][j])


# 3
# 10
# -7
# -4
# 4
# -8
# 6
# 8
# -4