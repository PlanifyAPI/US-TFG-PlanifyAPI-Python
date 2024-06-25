#!/bin/bash

#SBATCH -J test_restcountries
#SBATCH -o test_restcountries.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_restcountries.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
