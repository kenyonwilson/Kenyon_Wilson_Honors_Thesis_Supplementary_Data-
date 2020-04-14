for i in `ls *fa`; do
        echo $i |sed -e 's/.fa//g' |awk '{print ">"$0}' > sample_head
        myline=$(cat $i |awk -F "_" '{print $1}' |sed -e 's/-//g' |sed -e 's/\*//g' |awk '{print NR,length}' |sort -nr -k2 |head -n 1 |awk '{print $1}')
        sed -n ''$myline'p' $i |sed -e 's/-//g' |sed -e 's/\*//g' |paste -d "\n" sample_head - >> all.prots.fasta
done
