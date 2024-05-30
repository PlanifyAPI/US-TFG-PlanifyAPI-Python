#!/bin/bash

#SBATCH -J test_ohsome
#SBATCH -o test_ohsome.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_ohsome.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
