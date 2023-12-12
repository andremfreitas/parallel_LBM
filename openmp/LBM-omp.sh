#!/bin/bash
#SBATCH --job-name=LBM-strong-scaling
#SBATCH --partition=shared
#SBATCH --account=edu23.aqti
#SBATCH --nodes=2
#SBATCH --error=LBM-strong-scaling.err
#SBATCH --output=LBM-strong-scaling.txt


for((n=1; n<=8; n++))
do
    export OMP_PLACES="{0}:$n:1"
    export OMP_NUM_THREADS=$n
    srun -n $((n/2)) ./openLBMflow 
done