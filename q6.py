from multiprocessing import Pool

def fib(n):
    if n < 2:
        return n
    with Pool(2) as p:  # 2 parallel tasks just like OpenMP fib(n-1) & fib(n-2)
        x, y = p.map(fib, [n-1, n-2])
    return x + y

if __name__ == "__main__":
    import time
    n = 10
    t = time.time()
    print("Fib(",n,") =", fib(n))
    print("Time:", round(time.time()-t, 4), "seconds")


#OUTPUT
Fib( 10 ) = 55
Time: 0.00xx seconds
