#!/bin/bash

# Lista de archivos de test (obtenida de la imagen proporcionada)
tests=(
    "test_amadeus.py"
    "test_dhl.py"
    "test_fdic.py"
    "test_foursquare.py"
    "test_github.py"
    "test_language_tool.py"
    "test_marvel.py"
    "test_ohsome.py"
    "test_omdb.py"
    "test_restcountries.py"
    "test_spotify_5000.py"
    "test_spotify_5500.py"
    "test_spotify_6000.py"
    "test_stripe.py"
    "test_yelp.py"
    "test_youtube.py"
)

# Directorio de los tests
test_dir="PlanifyAPI.tests"

# Tiempo de ejecución
time="03-00:00:00"

# Crear un script SLURM para cada archivo de test
for test in "${tests[@]}"; do
    script_name="${test%.py}.sh"
    cat <<EOL > $script_name
#!/bin/bash

#SBATCH -J ${test%.py}
#SBATCH -o ${test%.py}.o%j
#SBATCH -t $time

date
echo "Corriendo script python"

python3 -m $test_dir.$test

echo "Finalizado el trabajo \$SLURM_JOBID"
date
EOL
done

