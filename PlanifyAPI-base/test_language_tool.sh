#!/bin/bash

#SBATCH -J test_language_tool
#SBATCH -o test_language_tool.o%j
#SBATCH -t 03-00:00:00

date
echo "Corriendo script python"

python3 -m PlanifyAPI.tests.test_language_tool.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
