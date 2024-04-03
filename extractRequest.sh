#!/bin/bash

#SBATCH -J parserJSON
#SBATCH -o parserJSON.o%j
#SBATCH -t 03:30:00

date
echo "Corriendo script python"

python3 extract_request.py

echo "Finalizado el trabajo $SLURM_JOBID"
date
