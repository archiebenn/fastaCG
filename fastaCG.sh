#!/bin/bash
#a bash script for URLs to .fa.gz (only - gzipped) files which will calculate the CG content from command line

set -e

# get cd
script_dir="$(cd "$(dirname "$0")" && pwd)"

# create venv
python3 -m venv "$script_dir/venv"

# activate venv
source "$script_dir/venv/bin/activate"

# install requirements
pip install -r "$script_dir/requirements.txt"

# make /data directory (/data/ in .gitignore)
mkdir -p data

# check if URL is provided
if [ -z "$1" ]; then
  echo "Error: No URL provided."
  echo "Usage: ./fastaCG.sh <URL-to-.fa.gz-file>"
  exit 1
fi

# downloads argument link from url (.fa.gz file), renames it to fasta.fa.gz, then gunzips it (creates a fasta.fa file)
wget "$1" -O "$script_dir/data/fasta.fa.gz" && gunzip "$script_dir/data/fasta.fa.gz"

# tells bash to run python script with fasta.fa as the argument  (structure: python script.py argument)
#therefore fasta.fa becomes sys.argv[1] in .py script
python3 "$script_dir/scriptFastaCGv2.py" "$script_dir/data/fasta.fa"


deactivate