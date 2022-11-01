import sys

K = 1
P = 2
N = 1

def po(p, n):
    q, r = divmod(n, 2)
    print('n:{}, q:{}, r:{}'.format(n, q, r))
    tmp = p * (n**q)

    if r == 0:
        return tmp * po(p, q)

    elif r == 1:
        return tmp * po(p, q) * p

    if q == 1:
        return p

    return po(p, int(q))


po(P, 10*N)