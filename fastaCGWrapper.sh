#!/bin/bash
#a bash script for URLs to .fa.gz (only - gzipped atm) files which will calculate the CG content from command line

#get cd
script_dir="$(cd "$(dirname "$0")" && pwd)"

# activate venv
source "$script_dir/venv/bin/activate"

#downloads argument link from url (.fa.gz file), renames it to fasta.fa.gz, then gunzips it (creates a fasta.fa file)
wget "$1" -O "$script_dir/fasta.fa.gz" && gunzip "$script_dir/fasta.fa.gz"

#tells bash to run python script with fasta.fa as the argument (sys.argv[1] in python)
#note that fasta.fa is the FILENAME (ie string literal), so .py script will need to open that file
python3 "$script_dir/fastaCG.py" "$script_dir/fasta.fa"


deactivate