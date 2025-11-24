from mpi4py import MPI

comm = MPI.COMM_WORLD
r = comm.Get_rank()

if r == 0:
    data = 99
    comm.send(data, dest=1)
    print("Rank 0 sent:", data)

elif r == 1:
    data = comm.recv(source=0)
    print("Rank 1 received:", data)


  
# OUTPUT
Rank 0 sent: 99
Rank 1 received: 99

