# FastaCG CLI Calculator

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
 - Run ./fastaCGWrapper https://ftp.ensembl.org/pub/current_fasta/sus_scrofa/dna/Sus_scrofa.Sscrofa11.1.dna.primary_assembly.Y.fa.gz
 - Overwrite fasta.fa
 - Outputs SEQUENCE NAME, GC PERCENTAGE:
[('Y dna:primary_assembly primary_assembly:Sscrofa11.1:Y:1:43547828:1 REF', 43.21423907651394)]
 - CG percentage ~43%
