#!/bin/bash

#SBATCH -J test_marvel
#SBATCH -o test_marvel.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_marvel.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
