#!/usr/bin/env python3
#above finds python using PATH
from Bio import SeqIO
import sys, time

start = time.perf_counter()

# Imput data from CLI (url to fa.gz)
fastaFile = sys.argv[1]

# Create empty dictionary and sequence count
percentCGdict = {}
totalSeqLength = 0

# Main loop
for record in SeqIO.parse(fastaFile, 'fasta'):
    seq = record.seq.upper()
    countA = seq.count('A')
    countT = seq.count('T')
    countC = seq.count('C')
    countG = seq.count('G')
    seqLength = len(seq)

    totalSeqLength += seqLength

    if seqLength == 0:
        percentCG = 0
    else :
        percentCG = ((countC + countG)/(countA + countT + countC + countG))*100
    
    percentCGdict[record.description] = percentCG

    
# Ouputting dictionary k-v pairs (sequence and percentage) to CLI
for sequence, cg in percentCGdict.items():
    print(f'\nSEQUENCE NAME: {sequence}: \nCG PERCENTAGE: {cg:.2f}%')


end = time.perf_counter()

print(f"Script took {end - start:.2f}s for a length of {totalSeqLength} bases")
print()