###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: Main.py                                                               #
# Purpose: Handle exercise 2 objects                                          #
###############################################################################

import argparse
import src.exercise_2 as ex2
import src.mould_sequence as mld

def main():
    # outline argparse arguments
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        '-i', '--input', required = True, help='Input file')
    parser.add_argument(
        '-f', '--genbank_format', action='store_true',
        help='Reformat the sequence in gebank format')
    parser.add_argument(
        '-p', '--protein', action='store_true',
          help='Translate DNA sequence to amino acid sequence')
    parser.add_argument(
        '-c', '--reverse_complement', action='store_true',
          help='Convert sequence to the reverse complement')
    parser.add_argument(
        '-r', '--reading_frames', action='store_true',
          help='Return all 6 reading frames for a given sequence')
    parser.add_argument(
        '-b', '--base_counting', action='store_true',
          help='Count all mono-, di-, and tri-nucleotide instances in a seq.')
    parser.add_argument(
        '-g', '--gc_content', action='store_true',
          help='Return the GC-content of a given sequence as a percentage')
    args = parser.parse_args()

    # open and read the txt file containing sequence
    sequence = open(args.input, 'r')
    sequence = sequence.read()

    # initialise mold sequence by passing the raw sequence in
    mould_obj = mld.mould_sequence(sequence)
    # using mol_sequence, return a corrected standard sequence format
    corrected_seq = mould_obj.seq_mould() #add seq_errors
    # print non-conformities and corrective actions to the terminal
    #print(seq_errors)

    # initialise exercise 2 object
    ex2_obj = ex2.exercise_2(corrected_seq)
    # perform desired operations
    if args.genbank_format == True:
        genbank_format = ex2_obj.genbank_convert()
    if args.protein == True:
        amino_acids = ex2_obj.DNA_to_protein()
    if args.reverse_complement == True:
        reverse = ex2_obj.reverse_seq()
    if args.reading_frames == True:
        six_frame = ex2_obj.sixFrame_translate()
    if args.base_counting == True:
        base_counts = ex2_obj.count_bases()
    if args.gc_content == True:
        gc_content = ex2_obj.gc_content()
    # add if no arguments selected consequence here

if __name__ == '__main__':
    main()
