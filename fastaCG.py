#!/usr/bin/env python3
#above finds python using PATH
import sys

# 0. INPUT DATA
fastaFile = sys.argv[1] #from bash script (it's always just fasta.fa here - don't actually need to use sys.argv but why not)
data = open(fastaFile, 'r')

#1. dividing FASTA strings:
seq = data.read()
#print(seq)
sequences = seq.split('>') #splits at '>' and removes '>'



#1.5 getting header for each new sequence in .fa file (so key, value pair gives key as actual sequence name in fasta file)
headers= []

for entry in sequences:
    newlineEntry = entry.find('\n') #finds newline after header
    if newlineEntry != -1:  #if '/n' isn't found find() returns -1. so if != -1 then it has found a '/n'
        header = entry[:newlineEntry] #names header for that entry to end at newline
        headers.append(header) #appends to headers list above




#2. cleaning up the strings in the list (removing \n)
#this removes first sequence as it's empty from > split at start of .fa file
if sequences[0] == '':
    sequences.remove(sequences[0])
    
for i in range(len(sequences)):
    sequences[i] = sequences[i].replace('\n', '') #removes \n


#3. Computing GC Content of divided strings and storing in dictionary
#creating empty lists of length len(sequences) ie. number of sequences
countA = [0] * len(sequences) #equivalent to [0, 0, 0] if 3 sequences etc.
countT = [0] * len(sequences)
countC = [0] * len(sequences)
countG = [0] * len(sequences)
countCG = [0] * len(sequences)
countAT = [0] * len(sequences)
countTotal = [0] * len(sequences)
percentCG = [0] * len(sequences)

#making a dictionary to assign string code to percentage of GC in each string
sequencePercentCGDict = {}

#looping over each string in list and counting bases/calculating CG percentages
for i in range(len(sequences)):
    # Count occurrences within each individual sequence
    countA[i] = sequences[i].count('A')
    countT[i] = sequences[i].count('T')
    countC[i] = sequences[i].count('C')
    countG[i] = sequences[i].count('G')

    countCG[i] = countC[i] + countG[i]
    countAT[i] = countA[i] + countT[i]

    countTotal[i] = countCG[i] + countAT[i]
    percentCG[i] = (countCG[i]/countTotal[i])*100

    #storing in dictionary (name and percentCG)
    seqName = headers[i]
    sequencePercentCGDict[seqName] = percentCG[i]





#4. sorting the dictionary by value number :0
sortedSequencepercentCGDict = sorted(sequencePercentCGDict.items(),
                                     key = lambda x:x[1],
                                     reverse = True)                                    
print()
print('SEQUENCE NAME, GC PERCENTAGE:')
print(sortedSequencepercentCGDict)