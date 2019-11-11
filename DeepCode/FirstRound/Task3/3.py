A = int(input())
table1 = list()
for i in range(1, A + 1):
    table1.append(int(input()))
B = int(input())
line = list()
line.append(table1[0])
line2 = list()
line2.append(1)
for i in range(1, B + 1):
    tmp = int(input())
    line.append(line[i-1]+tmp)
    if line2[i-1] <= 0 or tmp < 0:
        line2.append(0)
    else:
        line2.append(1)

for i in range(1, A):
    line[0] = table1[i]
    if line[i] < 0:
        line2[0] = 0
    else:
        line2[0] = 1
    for j in range(1, B + 1):
        line[j] = line[0] + line[j]
        line2[j] = (line2[j] + line2[j-1]) % 1000000007
print(line2[len(line2)-1])