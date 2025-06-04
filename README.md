# FastaCG CLI Calculator (mini tool)

Mini tool to calculate CG content of a FASTA sequence(s) from the command line using the URL to the .fa.gz file

## Requirements
- Python 3.x
- Biopython

## Usage
1. Clone the repository.
2. Navigate to the project directory.
3. Copy URL to .fa.gz file (for example from https://ftp.ensembl.org/pub/current_fasta/)
4. Run the script using the following command:

```bash
./fastaCG.sh <URL-to-.fa.gz-file>
```
## Example
For example, using the .fa.gz of a Wild Boar Y chromosome primary assembly from ensembl:
 - Copy url: https://ftp.ensembl.org/pub/current_fasta/sus_scrofa/dna/Sus_scrofa.Sscrofa11.1.dna.primary_assembly.Y.fa.gz
 - Run the following: ./fastaCG.sh https://ftp.ensembl.org/pub/current_fasta/sus_scrofa/dna/Sus_scrofa.Sscrofa11.1.dna.primary_assembly.Y.fa.gz
 - Select 'y' to overwrite existing fasta.fa file in project directory
 - Outputs:
   ```bash
   SEQUENCE NAME: Y dna:primary_assembly primary_assembly:Sscrofa11.1:Y:1:43547828:1 REF:
   CG PERCENTAGE: 43.21%
   TOTAL FASTA LENGTH: 43547828 bases"
   TIME: 0.67s
   ```
 - CG percentage output at 43.21%

## How it works
 - When the executable ./fastaCG.sh is run with a <URL-to-.fa.gz-file> from the command line, the link is downloaded using wget, renamed to 'fasta.fa.gz', and then gunzipped to leave the file 'fasta.fa'.
 - This fasta.fa file is then passed on to fastaCG.py, where the FASTA data are divided and cleaned, and the bases are counted to give a CG percentage.
 - The output of fastaCG.py gives the name of the sequence(s) from the FASTA file, followed by the CG percentage of that sequence.

## Version History
v1 - completed December 2024
- Manual parsing of FASTA file using string methods.
- Separately counts each base string 'A', 'T', 'C', 'G' in lists.
- Manually constructs sequence headers and splits on '>'.
- Ignored lowercase bases, occassionally leading to inaccurate percentages.

v2 - completed June 2025
- Uses Biopython's SeqIO to parse FASTA for more biologically reliable and accurate parsing.
- Simplifies base counting logic to directly calculate CG percentage.
- Case-insensitive to include all bases in FASTA file.
- Includes time taken and total base count for the FASTA file.
- Slightly faster. For example on https://ftp.ensembl.org/pub/current_fasta/caenorhabditis_elegans/dna/Caenorhabditis_elegans.WBcel235.dna.toplevel.fa.gz:  
  v1 - Script took 1.56s for a length of 100286799 bases (slightly overcounted)  
  v2 - Script took 1.29s for a length of 100286401 bases (accurate base count)
