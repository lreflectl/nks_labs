#
# P1 = 0.46
# P2 = 0.58
# P3 = 0.86
# P4 = 0.99
# P5 = 0.83
# P6 = 0.79
# P7 = 0.40
# P8 = 0.42
# P9 = 0.91
#
# P23 = 1 - (1 - P2)*(1 - P3)
# P45 = 1 - (1 - P4)*(1 - P5)
# P49 = 1 - (1 - P4)*(1 - P9)
# P59 = 1 - (1 - P5)*(1 - P9)
# P123 = P1*P23
# P598 = P59*P8
# P497 = 1 - (1 - P49)*(1 - P7)
# P49598 = 1 - (1 - P49)*(1 - P598)
# P7598 = 1 - (1 - P7)*(1 - P598)
# P4549598 = P45*P49598
# P75989 = P7598*P9
# P0 = 1 - (1 - P497)*(1 - P4549598)
# Presult = P123*P0*P75989
# print(round(Presult, 8))

inp = sorted([18, 27, 20, 18, 22, 20, 17, 24, 28, 23, 25, 22, 14, 24, 18, 33, 17, 19, 28, 23])
t = 29
k = 3

i_max = max(inp)
print(i_max)
i_min = min(inp)
print(i_min)
avg = sum(inp)/len(inp)
h = (i_max-i_min)/k
print(h)

intervals = []
for i in range(k):
    intervals.append((i_min + round(i*h, 3), i_min + round((i+1)*h, 3)))
print(intervals)

index_i = 0
for i in intervals:
    if i[0] <= t <= i[1]:
        index_i = intervals.index(i)

print(index_i, intervals[index_i])

counter = 0
for t in inp:
    if intervals[index_i][0] <= t <= intervals[index_i][1]:
        counter += 1

print(counter)
f = counter/(len(inp)*h)
print(f)
print(len(inp))
