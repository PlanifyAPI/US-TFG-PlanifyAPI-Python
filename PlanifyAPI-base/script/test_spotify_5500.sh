#!/bin/bash

#SBATCH -J test_spotify_5500
#SBATCH -o test_spotify_5500.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_spotify_5500.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
