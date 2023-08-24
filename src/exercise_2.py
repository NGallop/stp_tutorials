###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: exercise2.py                                                          #
# Purpose: Handle exercise 2 methods within an object                         #
###############################################################################


# object to house all exercise 2 methods
class exercise_2():

    def __init__(self, incoming_sequence):
        self.sequence = incoming_sequence

    # 2.1: convert fasta DNA base string to GenBank records style. 
    # e.g. "ACTGACTGACTGACTGACTG" > '1 actgactgac tgactgactg actgactgac'
    def genbank_convert(self):
        return
    
    # 2.2: translate DNA sequence to amino acid sequence
    # e.g. aggagtaag > RSK, or AGGAGTAAG > RSK
    def DNA_to_protein(self):
        return
    
    # 2.3 generate the reverse complement of a sequence
    # e.g. aggagtaag > cttactcct
    def reverse_seq(self):
        return
    
    # 2.4 generate a six-frame translation of a sequence
    # e.g. Forward: RSK, GVS, E*A; Reverse: LTP, GLL, AYS
    def sixFrame_translate(self):
        return
    
    # 2.5 count mono-, di- and tri-nucleotides in a sequence
    # e.g. a 12, g 9, t 7... ag 1, ga 1, gt 2, aa 3... acg 1, att 1, agt 1...
    def count_bases(self):
        return
    
    # 2.6 generate GC-content % of a sequence
    # e.g. acctaggccat > GC-content = 50%
    def gc_content(self):
        return