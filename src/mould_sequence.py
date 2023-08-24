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

    def __remove_whitespace(str):
        seq = " ".join(str.splitlines())
        seq = seq.replace(" ", "")
        return seq

    def __remove_numbers(str):
        return

    def __character_check(str):
        accepted_chars = set('ATCGatcg')
        expected_char = set('Nn')
        return

    # accept any sequence and mold into format ACGTACGTACGT
    def seq_mould(self):
        seq = self.input_sequence
        seq = self.__remove_whitespace(seq)
        seq = self.__remove_numbers(seq)
        seq = self.__character_check(seq)
        return seq

def main():
    return

if __name__ == '__main__':
    main()