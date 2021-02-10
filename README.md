# rosalind_shared_DNA_motif
Finds the longest common substring shared by a list of DNA sequences.

This code is a solution to the Finding a Shared Motif (ID - LCSM) problem on the bioinformatics website Rosalind.

The code takes input of a text file listing DNA sequences in FASTA format.
It searches through all sequences in the list and out puts a text file containing the longest sequence that is common to the entire list.

This program is an improvement of the code found in the main branch which could theoretically return the correct answer but could only do so in an unreasonable timeframe.
The code in this branch should run in less than 5 seconds for list of 100 DNA sequences of approximately 1000 bases each. 
