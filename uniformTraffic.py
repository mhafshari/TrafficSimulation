###################################


# written by @mhafshari
# simulating uniform traffic on switches and routers
# At every time slot for each input, a packet arrives with
# probability p (input load p) and destines to each output with equal probability.

###################################


import random

print("enter p: ")
p = float(input())
print("enter N(switch size like 4 , 8): ")
N = int(input())
queue = [[0] * N for i in range(N)]
for T in range(100):
    print("time slot: " + str(T))
    if T % 10 == 0:
        send_time_slot = [[0] * 10 for i in range(N)]
        for u in range(N):
            send_time_slot[u] = random.sample(range(0, 10), int(p * 10))
            if 0 in send_time_slot[u]:
                j = random.randrange(1, N, 1)
                queue[u][j] = queue[u][j] + 1
                print(str(u) + "->" + str(j))
    else:
        for u in range(N):
            if T % 10 in send_time_slot[u]:
                j = random.randrange(1, N, 1)
                queue[u][j] = queue[u][j] + 1
                print(str(u) + "->" + str(j))
