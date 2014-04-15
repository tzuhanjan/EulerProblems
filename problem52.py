def digitDicMaker(x):
    k = {}
    for z in xrange(10):
       k[str(z)] = 0
    for a in str(x):
        k[a] += 1
    return k

def equalChecker(x, y):
    for a in xrange(10):
        if x[str(a)] != y[str(a)]:
            return False
    return True

x = 1
while True:
    flag = True
    for y in xrange(3,7):
        if not equalChecker(digitDicMaker(2*x), digitDicMaker(x*y)):
            flag = False
            break
    if flag:
        print x
        break
    x += 1
