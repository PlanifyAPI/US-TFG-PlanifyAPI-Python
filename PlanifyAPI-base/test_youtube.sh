#!/bin/bash

#SBATCH -J test_youtube
#SBATCH -o test_youtube.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_youtube.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
