#!/bin/bash

#SBATCH -J test_yelp
#SBATCH -o test_yelp.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_yelp.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
