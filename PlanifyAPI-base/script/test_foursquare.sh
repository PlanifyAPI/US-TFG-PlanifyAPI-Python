#!/bin/bash

#SBATCH -J test_foursquare
#SBATCH -o test_foursquare.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_foursquare.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
