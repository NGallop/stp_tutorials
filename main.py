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
    # check if arguments have been selected and abort program if not
    if selected_args == [False, False, False, False, False, False]:
        print("No arguments selected, aborting program")
        quit()

    # open and read the txt file containing sequence
    try:
        sequence = open(cli_obj.args.input, 'r')
        sequence = sequence.read()
    except FileNotFoundError:
        print("ERROR: input file not found, please check input")
        quit()

    # hardcoded codon table
    quitter = 0
    try:
        with open ('ref/codon.json', 'r') as f:
            codon_json = json.load(f)
    except FileNotFoundError:
        print("Warning: could not load codon table. Codon table must be located at ref/codon.json. \n")
        codon_json = {}
        quitter = 1

    # initialise mold sequence by passing the raw sequence in
    mould_obj = mld.mould_sequence(sequence)
    # using mol_sequence, return a corrected standard sequence format
    corrected_seq = mould_obj.seq_mould() 
    
    # initialise exercise 2 object
    ex2_obj = ex2.exercise_2(corrected_seq, codon_json)
    # perform desired operations
    if selected_args[0] == True:
        genbank_format = ex2_obj.genbank_convert()
        print("Genbank format: \n", genbank_format, "\n")
    if selected_args[1] == True:
        if quitter > 0:
            print('ERROR: Codon table required for function. \n')
        else:
            amino_acids = ex2_obj.DNA_to_protein()
            print("Translation: \n", amino_acids, "\n")
    if selected_args[2] == True:
        reverse = ex2_obj.reverse_seq()
        print('Forward (original):\n', corrected_seq)
        print('Reverse:\n', reverse, "\n")
    if selected_args[3] == True:
        if quitter > 0:
            print('ERROR: Codon table required for function. Program aborted. \n')
        else:
            six_frame = ex2_obj.sixFrame_translate()
            print("Six-frame translation dictionary: \n", six_frame, "\n")
    if selected_args[4] == True:
        base_counts = ex2_obj.count_bases()
        print("base counts: ", base_counts, "\n")
    if selected_args[5] == True:
        gc_content = ex2_obj.gc_content()
        print("GC-content is: ", gc_content, "% \n")


if __name__ == '__main__':
    main()
