from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()

val = r + 1   # simple value for demonstration

# Reduce (results only at root)
mx = comm.reduce(val, op=MPI.MAX, root=0)
mn = comm.reduce(val, op=MPI.MIN, root=0)
sm = comm.reduce(val, op=MPI.SUM, root=0)
pr = comm.reduce(val, op=MPI.PROD, root=0)

if r == 0:
    print("=== MPI_Reduce Results ===")
    print("Max =", mx)
    print("Min =", mn)
    print("Sum =", sm)
    print("Prod =", pr)

# Allreduce (results at ALL ranks)
mx2 = comm.allreduce(val, op=MPI.MAX)
mn2 = comm.allreduce(val, op=MPI.MIN)
sm2 = comm.allreduce(val, op=MPI.SUM)
pr2 = comm.allreduce(val, op=MPI.PROD)

print(f"Rank {r}: Max={mx2}, Min={mn2}, Sum={sm2}, Prod={pr2}")


#OUTPUT
=== MPI_Reduce Results ===
Max = 4
Min = 1
Sum = 10
Prod = 24
Rank 0: Max=4, Min=1, Sum=10, Prod=24
Rank 1: Max=4, Min=1, Sum=10, Prod=24
Rank 2: Max=4, Min=1, Sum=10, Prod=24
Rank 3: Max=4, Min=1, Sum=10, Prod=24

