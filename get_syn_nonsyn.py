# use it under python2.7
  
import numpy as np ;
import egglib ;
import sys ;
import pickle

aln1 = egglib.io.from_fasta(sys.argv[1], cls=egglib.Align, groups=True) # opens alignment file
print aln1.ls ; aln1.ns       # prints overall length sequence (ls) and number of sequences (ns)
cdiv = egglib.stats.CodingDiversity(aln1)   # identifies the sequence as a coding element -meaning it has a triplet codon structure
nonsyn = cdiv.mk_align_NS() # identifies those parts of the alignment that are non-synonymous
syn = cdiv.mk_align_S()   # identifies those parts of the alignment that are synonymous

nonsyn_n = cdiv.num_sites_NS  #  captures the number of non-synonymous codons
syn_n = cdiv.num_sites_S     # captures the number of synonymous codons

myfile=sys.argv[1]

print myfile;

print nonsyn_n   #  prints the number of non-synonymous codons
f1 = open("nonsyn_Tn.tab", "a")  #  saves the number of non-synonymous codons in file
f1.write(str(myfile) + "\t" + str(nonsyn_n) + "\n")
f1.close()


print syn_n   # prints the number of synonymous codons
f2 = open("syn_Tn.tab", "a") #  saves the number of synonymous codons in file
f2.write(str(myfile) + "\t" + str(syn_n) + "\n")
f2.close()


####
# this is the complicated part.
# it separates and creates different data partitions for the  variable synonymous and non-synonymous sites so we can save them in separate files

mapping = {-1: 'NNN'}
for codon_code in range(64):
        codon = ''.join([egglib._eggwrapper.GeneticCode.base(codon_code, pos) for pos in (0,1,2)])
        mapping[codon_code] = codon
        mapping[egglib._eggwrapper.UNKNOWN] = 'NNN'


f = open("nonsyn.tab", "w")
for i in nonsyn:
        f.write("|".join([mapping[x] for x in i.sequence]) + "\n")

f.close()

f = open("syn.tab", "w")
for i in syn:
        f.write("|".join([mapping[x] for x in i.sequence]) + "\n")

f.close()

