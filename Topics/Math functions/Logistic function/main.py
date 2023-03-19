import math

num = int(input())
out = 1 / (1 + math.exp(-num))
print(round(out, 2))
