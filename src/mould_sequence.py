###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: mould_sequence.py                                                     #
# Purpose: Handle all exception and create standard format                    #
###############################################################################

class mould_sequence():

    # Set attributes
    def __init__(self, incoming_sequence):
        self.input_sequence = incoming_sequence

    # remove whitespace and line breaks from input sequence
    def __remove_whitespace(self):
        seq = " ".join(self.input_sequence.splitlines())
        seq = seq.replace(" ", "")
        return seq

    # capitalise any characters that are in lower case
    def __caps_char(self, in_seq):
        seq = in_seq.upper()
        return seq
    
    # remove numbers
    def __remove_numbers(self, in_seq):
        seq = ''.join(i for i in in_seq if not i.isdigit())
        return seq

    # check string only contains expected characters and return an error if not
    def __character_check(self, in_seq):
        accepted_chars = set('ATCGN')
        expected_char = set('N')
        seq = set(in_seq)
        # if the unique characters in sequence is a subset of the accepted characters set
        if seq.issubset(accepted_chars):
            # if any character in expected characters (N) if in any character in the unique character set
            if any(char in expected_char for char in seq):
                print('ERROR: degenerate/ambiguous base calls not supported. Sequence cannot contain N.')
                quit()
            else:
                pass
        else:
            print('ERROR: sequence contains non-base characters. Cannot process.')
            quit()
        return in_seq

    # accept any sequence and mold into format ACGTACGTACGT
    def seq_mould(self):
        seq = self.__remove_whitespace()
        seq = self.__caps_char(seq)
        seq = self.__remove_numbers(seq)
        seq = self.__character_check(seq)
        return seq