#!/bin/bash
#a bash script for URLs to .fa.gz (only - gzipped atm) files which will calculate the CG content from command line
# activate venv
source /home/ab/Dropbox/coding/shellin/fastaCG/venv/bin/activate

#downloads argument link from url (.fa.gz file), renames it yo fasta.fa.gz, then gunzips it (creates a fasta.fa file)
wget "$1" -O fasta.fa.gz && gunzip fasta.fa.gz

#tells bash to run python script with fasta.fa as the argument (sys.argv[1] in python)
#note that fasta.fa is the FILENAME (ie string literal), so .py script will need to open that file
python3 /home/ab/Dropbox/coding/shellin/fastaCG/fastaCG.py fasta.fa


deactivate