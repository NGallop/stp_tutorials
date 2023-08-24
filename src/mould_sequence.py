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

    def __remove_whitespace(self):
        seq = " ".join(self.input_sequence.splitlines())
        seq = seq.replace(" ", "")
        return seq

    def __character_check(self, no_wsno_seq):
        accepted_chars = set('ATCGatcg')
        expected_char = set('Nn')
        return

    # accept any sequence and mold into format ACGTACGTACGT
    def seq_mould(self):
        seq = self.__remove_whitespace()
        #seq = self.__character_check(seq)
        return seq

def main():
    sequence = open('ref/sequence_ws.txt', 'r')
    sequence = sequence.read()
    mould_obj = mould_sequence(sequence)
    corrected_seq = mould_obj.seq_mould()
    print(corrected_seq)

if __name__ == '__main__':
    main()