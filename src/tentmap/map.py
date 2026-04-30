

def G(x,*, A):
    assert (x >= 0 and x <= 1), "boundaries of x are [0, 1]"
    assert (A >= 0 and A <= 2), "boundaries of A are [0, 2]"

    if 0 < x < 1/2:
        return A*x
    else:
        return A*(1-x)

def Gn(x, N, *, A):
    for _ in range(N):
        x = G(x, A=A)
        if x >= 1:
            x = 1
    return x

