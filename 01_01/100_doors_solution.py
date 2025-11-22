def hundred_doors(n=100):
    doors = [False] * (n + 1)  # False=closed, True=open; index 1..n
    for r in range(1, n + 1):
        for d in range(r, n + 1, r):
            doors[d] = not doors[d]
    open_doors = [i for i in range(1, n + 1) if doors[i]]
    return open_doors
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(hundred_doors()) 


#Author Solution:
doors = [False]*101 # So we cqn start at door no.1.We will ignore index 0

for i in range(1,101):
    for j in range(i,101,i):
        doors[j] = not doors[j]

for i in range(1, 101):
    if doors[i] is True:
        print(i, end=",")