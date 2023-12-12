#!/bin/bash
#SBATCH --job-name=LBM-strong-scaling
#SBATCH --partition=shared
#SBATCH --account=edu23.aqti
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32 
#SBATCH --error=LBM-strong-scaling.err
#SBATCH --output=LBM-strong-scaling.txt

# export OMP_NUM_THREADS=1
# srun -n 1 -N 1 ./LBM-omp

for((n=1; n<=8; n++))
do
    export OMP_PLACES="{0}:$n:1"
    export OMP_NUM_THREADS=$n
    srun -n 1 -N 1 ./LBM-omp
done