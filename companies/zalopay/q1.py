# Enter your code here. Read input from STDIN. Print output to STDOUT
# 104,99,76,94,78,77,75

cases = [int(c) for c in input().split(",")]
cases.append(float("inf"))
result = []

for i in range(len(cases) - 1):
    j = i + 1
    while (j < len(cases) - 1) & (cases[j] >= cases[i]):
        j += 1
    if cases[j] != float("inf"):
        result.append(j - i)
    else:
        result.append(-1)

print(",".join([str(x) for x in result]))
