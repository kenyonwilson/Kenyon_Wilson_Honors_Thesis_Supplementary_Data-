#for i in `cat list`; do
for i in `ls *.aln`; do
        python2.7 get_syn_nonsyn.py $i ;
        R CMD BATCH generate_counts.R
done
