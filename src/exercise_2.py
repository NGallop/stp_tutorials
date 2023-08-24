###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: exercise2.py                                                          #
# Purpose: Object to house all exercise 2 methods                             #
###############################################################################

class exercise_2():

    def __init__(self, incoming_sequence, codon_dict):
        self.sequence = incoming_sequence
        self.codon_table = codon_dict

    # 2.1: convert fasta DNA base string to GenBank records style. 
    # e.g. "ACTGACTGACTGACTGACTG" > '1 actgactgac tgactgactg actgactgac'
    def genbank_convert(self):
        return
    
    # 2.2: translate DNA sequence to amino acid sequence
    # e.g. aggagtaag > RSK, or AGGAGTAAG > RSK
    def DNA_to_protein(self):
        amino_list = []
        seq = self.sequence
        n = range(len(seq))
        for i in n[::3]:
            x = seq[i:][:3]
            aa = self.codon_table[x]
            amino_list.append(aa)
        amino_acid_sequence = "".join(amino_list)
        return amino_acid_sequence
    
    # 2.3 generate the reverse complement of a sequence
    # e.g. aggagtaag > cttactcct
    def reverse_seq(self):
        seq = self.sequence
        seqOut = ""
        for base in seq:
            if base == "A":
                outbase = "T"
            elif base == "T":
                outbase = "A"
            elif base == "C":
                outbase = "G"
            elif base == "G":
                outbase = "C"
            else:
                outbase = base
            seqOut=outbase+seqOut
        return seqOut

    
    # 2.4 generate a six-frame translation of a sequence
    # e.g. Forward: RSK, GVS, E*A; Reverse: LTP, GLL, AYS
    def sixFrame_translate(self):
        return
    
    # 2.5 count mono-, di- and tri-nucleotides in a sequence
    # e.g. a 12, g 9, t 7... ag 1, ga 1, gt 2, aa 3... acg 1, att 1, agt 1...
    def count_bases(self):
        seq = self.sequence
        codons = self.codon_table
        mono_char = ['A', 'T', 'C', 'G']
        di_char = ['AA', 'AT', 'AC', 'AG', 'TA', 'TT', 'TC', 'TG', 'CA', 'CT',\
                   'CC', 'CG', 'GA', 'GT', 'GC', 'GG']
        tri_char = dict.keys(codons)
        count_dict = {}
        for base in mono_char:
            dnaCount = seq.count(base)
            count_dict["{0}".format(base)] = dnaCount
        for base in di_char:
            dnaCount = seq.count(base)
            count_dict["{0}".format(base)] = dnaCount
        for base in tri_char:
            dnaCount = seq.count(base)
            count_dict["{0}".format(base)] = dnaCount

        return count_dict
    
    # 2.6 generate GC-content % of a sequence
    # e.g. acctaggccat > GC-content = 50%
    def gc_content(self):
        seq = self.sequence
        dic = {}
        for i in "ACGT":
            dnaCount = seq.count(i)
            dic["{0}".format(i)] = dnaCount

        total = dic["A"]+dic["C"]+dic["G"]+dic["T"]
        GC = dic["C"]+dic["G"]
        perc = (GC/total)*100
        return perc