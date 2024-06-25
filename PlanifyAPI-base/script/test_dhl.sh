#!/bin/bash

#SBATCH -J test_dhl
#SBATCH -o test_dhl.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_dhl.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
