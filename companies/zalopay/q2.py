# Enter your code here. Read input from STDIN. Print output to STDOUT


N = int(input())
families = []
for _ in range(N):
    families.append([int(x) for x in input().split(",")])


queues = [0]

while families:
    family = families[0]
    families = families[1:]

    new_queue = True
    # queues = sorted(queues)
    for i, end_time in enumerate(queues):
        if end_time < family[0]:
            # Update new end_time
            queues[i] = family[0] - 1 + family[1]
            new_queue = False
            break
        elif (end_time - family[0] + 1) + family[1] <= 9:
            # Update new end_time
            queues[i] = end_time + family[1]
            new_queue = False
            break
    if new_queue:
        queues.append(family[0] - 1 + family[1])

print(len(queues))
