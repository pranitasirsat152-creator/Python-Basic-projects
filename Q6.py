import random
import math

try:
    s = set()

    print("Enter 10 Numbers")
    for i in range(10):
        n = int(input())
        s.add(n)

    t = tuple(s)

    print("Tuple:", t)

    print("3 Random Numbers:")
    print(random.sample(t, min(3, len(t))))

    total = sum(t)
    print("Square Root:", math.sqrt(total))

except Exception as e:
    print("Error:", e)
