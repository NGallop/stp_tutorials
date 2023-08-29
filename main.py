###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: Main.py                                                               #
# Purpose: Handle exercise 2 objects                                          #
###############################################################################

import json
import sys
import src.exercise_2 as ex2
import src.mould_sequence as mld
import src.cli as cli

def main():

    # initialise cli object
    cli_obj = cli.cli_obj(sys.argv[1:])
    selected_args = cli_obj.arg_selection()
    if selected_args == [False, False, False, False, False, False]:
        print("No arguments selected, aborting program")
        quit()

    # open and read the txt file containing sequence
    sequence = open(cli_obj.args.input, 'r')
    sequence = sequence.read()

    # initialise mold sequence by passing the raw sequence in
    mould_obj = mld.mould_sequence(sequence)
    # using mol_sequence, return a corrected standard sequence format
    corrected_seq = mould_obj.seq_mould() 

    # hardcoded codon table
    with open ('ref/codon.json', 'r') as f:
        codon_json = json.load(f)
    
    # initialise exercise 2 object
    ex2_obj = ex2.exercise_2(corrected_seq, codon_json)
    # perform desired operations
    if selected_args[0] == True:
        genbank_format = ex2_obj.genbank_convert()
        print(genbank_format)
    if selected_args[1]== True:
        amino_acids = ex2_obj.DNA_to_protein()
        print(amino_acids)
    if selected_args[2] == True:
        reverse = ex2_obj.reverse_seq()
        print('Forward:\n', corrected_seq)
        print('Reverse:\n', reverse)
    if selected_args[3] == True:
        six_frame = ex2_obj.sixFrame_translate()
        print(six_frame)
    if selected_args[4] == True:
        base_counts = ex2_obj.count_bases()
        print("base counts: ", base_counts)
    if selected_args[5] == True:
        gc_content = ex2_obj.gc_content()
        print("GC-content is: ", gc_content, "%")


if __name__ == '__main__':
    main()
