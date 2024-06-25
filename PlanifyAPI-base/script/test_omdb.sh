#!/bin/bash

#SBATCH -J test_omdb
#SBATCH -o test_omdb.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_omdb.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
