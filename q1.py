from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
if r == 0:
    comm.send(99, dest=1)
    print("Rank 0 Sent")
else:
    x = comm.recv(source=0)
    print("Rank 1 Received", x)

  
# OUTPUT
Rank 0 Sent
Rank 1 Received 99
