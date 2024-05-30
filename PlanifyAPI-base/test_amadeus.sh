#!/bin/bash

#SBATCH -J test_amadeus
#SBATCH -o test_amadeus.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_amadeus.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
