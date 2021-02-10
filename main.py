# This code is intended to find the longest DNA motif shared by a list of DNA sequences.
# It technically works in its current form but the computational time required for anything more than a short list of
# short sequences is unreasonable.

import re


# Class to create objects storing the id and DNA sequence of DNA strings in FASTA format.
class FastaObj:
    def __init__(self, fasta_id, sequence):
        self.fasta_id = fasta_id
        self.sequence = sequence

    def get_id(self):
        return self.fasta_id

    def get_seq(self):
        return self.sequence


# Take DNA strings in FASTA format from a text file and store them as a FastaObj in a list.
def create_fasta_list(file_name):
    file = open(file_name, "r")

    current_id = ""
    current_seq = ""
    fasta_list = []

    # Iterate through text file storing DNA strings in FASTA format and identify start of new FASTA ID
    # and corresponding DNA sequence.
    # New FASTA ID is denoted by ">". All following lines are added to the corresponding DNA sequence until
    # a new ">" chevron symbol is found.
    for line in file:
        if line[0] == ">" and current_id == "":
            current_id = line[1:].rstrip()
        elif line[0] == ">" and current_id != "":
            fasta_list.append(FastaObj(current_id, current_seq))
            current_id = line[1:].rstrip()
            current_seq = ""
        else:
            current_seq += line.rstrip()
    else:
        fasta_list.append(FastaObj(current_id, current_seq))

    file.close()
    return fasta_list


# Takes a list of FastaObj objects and returns the longest common substring.
def find_lcs(input_list):
    lcs = ""
    # Go through each DNA sequence in the list.
    for line in range(len(input_list)):
        fasta = input_list[line]
        sequence = fasta.get_seq()
        seq_length = len(sequence)
        # Iterate through all possible substrings.
        for index1 in range(seq_length+1):
            for index2 in range(index1, seq_length):
                test_seq = sequence[index1:index2+1]
                print(test_seq)
                # print(f"index1 is {index1}, index2+1 is {index2+1}")
                matches_all_lines = False

                # Iterate through all other DNA sequences in the list and see if the current substring is found in all
                # of them.
                for test_line in range(line+1, len(input_list)):
                    comp_fasta = input_list[test_line]
                    comp_seq = comp_fasta.get_seq()
                    # print(test_seq, comp_seq, lcs)
                    x = re.search(test_seq, comp_seq)
                    # print(x)
                    if x is not None:
                        # print(test_seq, comp_seq)
                        matches_all_lines = True
                    else:
                        matches_all_lines = False
                        break
                if matches_all_lines is True and len(test_seq) >= len(lcs):
                    lcs = test_seq
    return lcs


fasta_list = create_fasta_list("sample_fasta.txt")
# for line in fasta_list:
# print(line.get_id(), line.get_seq())
longest_common_substring = find_lcs(fasta_list)
print(longest_common_substring)
output = open("longest_common_substring.txt", "w")
output.write(longest_common_substring)
output.close()
