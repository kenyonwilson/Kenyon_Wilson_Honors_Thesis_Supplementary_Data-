for i in `ls *aln`; do
        java -jar /media/venezuela7/repository_software_recent/macse_v1.01b.jar -prog exportAlignment -align $i -codonForFinalStop --- -codonForInternalStop NNN
done
