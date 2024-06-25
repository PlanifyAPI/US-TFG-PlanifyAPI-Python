#!/bin/bash

#SBATCH -J test_fdic
#SBATCH -o test_fdic.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_fdic.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
