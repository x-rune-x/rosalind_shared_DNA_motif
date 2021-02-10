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
def find_substrings(input_list):
    common_substrings = []

    # Check if the first and second sequence share any substrings. If they don't we can return an null.
    # If they do, we can check if any are shared with all the sequences in the list.

    fasta1 = input_list[0]
    fasta2 = input_list[1]

    seq1 = fasta1.get_seq()
    seq_length1 = len(seq1)

    sequence2 = fasta2.get_seq()

    # Iterate through all possible substrings of the first sequence in the list and check if it is found in the second.
    for index1 in range(seq_length1):
        for index2 in range(index1, seq_length1):
            test_seq = seq1[index1:index2+1]

            init_match = re.search(test_seq, sequence2)
            if init_match:
                add_to_list = False

                # Check if substring is found in all other sequences and if so add to list of common substrings.
                for sequence in range(len(input_list)):
                    check_seq = input_list[sequence].get_seq()
                    is_match = re.search(test_seq, check_seq)
                    if is_match:
                        add_to_list = True
                    else:
                        add_to_list = False
                        break
                if add_to_list and len(test_seq) > 1:
                    common_substrings.append(test_seq)
            else:
                break

    return common_substrings


def find_list_maxlength(substring_list):
    longest_substring = ""
    longest_length = 0
    for line in substring_list:
        if len(line) > longest_length:
            longest_substring = line
            longest_length = len(line)

    return longest_substring


test_fasta_list = create_fasta_list("rosalind_lcsm.txt")
test_ss_list = find_substrings(test_fasta_list)
lcs = find_list_maxlength(test_ss_list)
print(lcs)

output_file = open("lcs.txt", "w")
output_file.write(lcs)
output_file.close()

