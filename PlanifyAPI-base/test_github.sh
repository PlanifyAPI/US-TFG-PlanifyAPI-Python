#!/bin/bash

#SBATCH -J test_github
#SBATCH -o test_github.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_github.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
