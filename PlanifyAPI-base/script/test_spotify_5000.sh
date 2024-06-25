#!/bin/bash

#SBATCH -J test_spotify_5000
#SBATCH -o test_spotify_5000.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_spotify_5000.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
