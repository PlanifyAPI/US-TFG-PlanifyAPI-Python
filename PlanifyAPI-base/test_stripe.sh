#!/bin/bash

#SBATCH -J test_stripe
#SBATCH -o test_stripe.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_stripe.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
