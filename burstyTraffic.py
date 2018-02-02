###################################


# written by @mhafshari
# simulating bursty traffic on switches and routers
# Given the average input load
# of p and burst size w, the state transition probabilities from
# OFF to ON is p/[w(1 − p)] and from ON to OFF is 1/w.
# We set the burst size w = 30 packets.

###################################


import random
import math

print("enter p: ")
p = float(input())
print("enter N (switch size like 4 , 8): ")
N = int(input())
queue = [[0] * N for i in range(N)]
n = math.ceil(N * p)
on = [0] * n
off = [0] * n
out_port = [0] * N
input_arrive = [0] * N

input_unique = random.sample(range(0, N), n)
for T in range(100):
    print("time slot: " + str(T))
    for k in range(int(n)):
        if on[k] == 0 and off[k] == 0:
            on[k] = 30
            out_port[k] = random.randrange(0, N, 1)
            input_arrive[k] = input_unique[k]
            if p < 1:
                off[k] = random.randrange(1, ((30 * (1 - p)) / p) + 1, 1)
            else:
                off[k] = 0
        if on[k] > 0:
            queue[input_arrive[k]][out_port[k]] = queue[input_arrive[k]][out_port[k]] + 1
            print(str(input_arrive[k]) + "->" + str(out_port[k]))
            on[k] = on[k] - 1
        elif off[k] > 0:
            off[k] = off[k] - 1
