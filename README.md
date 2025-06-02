# FastaCG CLI Calculator (mini tool)

CG content of FASTA sequence(s) to be calculated from the command line using URL to the .fa.gz file.

## Requirements
- Python 3.x

## Usage
1. Clone the repository.
2. Navigate to the project directory.
3. Copy URL to .fa.gz file (for example from https://ftp.ensembl.org/pub/current_fasta/)
4. Run the script using the following command:

```bash
./fastaCGWrapper.sh <URL-to-.fa.gz-file>
```
## Example
For example, using the .fa.gz of a Wild Boar Y chromosome primary assembly from ensembl:
 - Copy url: https://ftp.ensembl.org/pub/current_fasta/sus_scrofa/dna/Sus_scrofa.Sscrofa11.1.dna.primary_assembly.Y.fa.gz
 - Run the following: ./fastaCGWrapper https://ftp.ensembl.org/pub/current_fasta/sus_scrofa/dna/Sus_scrofa.Sscrofa11.1.dna.primary_assembly.Y.fa.gz
 - Select Y to overwrite fasta.fa
 - Outputs:
   ```bash
   SEQUENCE NAME: Y dna:primary_assembly primary_assembly:Sscrofa11.1:Y:1:43547828:1 REF:
   CG PERCENTAGE: 43.21423907651394
   ```
 - CG percentage ~43.2%

## How it works
 - When the executable ./fastaCGWrapper is run with a <URL-to-.fa.gz-file> from the command line, the link is downloaded using wget, renamed to fasta.fa.gz, and then gunzipped to leave the file fasta.fa.
 - This fasta.fa is then passed on to fastaCG.py, where the FASTA data are divided and cleaned, and the bases are counted to give a CG percentage.
 - The output of fastaCG.py gives the name of the sequence(s) from the FASTA file, followed by the CG percentage of that sequence.

