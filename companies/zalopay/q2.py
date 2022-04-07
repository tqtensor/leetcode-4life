# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
families = []
for _ in range(N):
    families.append([int(x) for x in input().split(",")])

all_queues = []


def dfs(families, queues):
    if len(families) == 0:
        all_queues.append(queues)
        return

    family = families[0]
    families = families[1:]

    new_queue = True
    for i, end_time in enumerate(queues):
        if end_time < family[0]:
            _queues = queues.copy()
            _queues[i] = family[0] - 1 + family[1]
            new_queue = False
            dfs(families, _queues)
        elif (end_time - family[0] + 1) + family[1] <= 9:
            _queues = queues.copy()
            _queues[i] = end_time + family[1]
            new_queue = False
            dfs(families, _queues)

    if new_queue:
        _queues = queues.copy()
        dfs(families, _queues + [family[0] - 1 + family[1]])


queues = [0]
dfs(families, queues)
print(min(all_queues, key=len))
