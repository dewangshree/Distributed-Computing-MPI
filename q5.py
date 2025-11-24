from multiprocessing import Pool

N = 100

def f(i):
    return i

if __name__ == "__main__":
    s = sum(Pool().map(f, range(1, N+1)))
    print("Sum =", s)


#OUTPUT
500000500000
