import math
f = math.factorial
total = 0
for x in xrange(101):
    for y in xrange(x):
        if f(x) / f(y) / f(x-y) > 1000000:
            total += x-2*y + 1
            break
print total
