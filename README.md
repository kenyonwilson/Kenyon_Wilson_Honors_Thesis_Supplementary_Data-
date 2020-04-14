# These are the supplementary tables and data for my Honors Thesis (Spring 2020). 
 The different files quoted in my Honors Thesis (The role of selection on determining the genomic diversity of Gardnerella vaginalis, Spring 2020) at Washington State University can be found in this repository. 
1.	The file titled data_hyphy.xlsx lists all of the results from the results from the HyPhy program with BUSTED functioning. 
2.	The file titled enrichment_core_genome.xlsx contains the results of the Fisher’s Exact test done on the enrichment of the core genome. 
3.	The file titled enrichment_multi_selection.xlsx contains the results of the Fisher’s Exact test done on the enrichment of the dispensable genome. 
4.	The generate_counts.R file is a script developed by Dr. Cornejo that was used to create the output of synonymous and nonsynonymous variable sites and the synonymous sites were used to create the site frequency spectrum.
5.	The get_syn_nonSyn.sh file combined the generate_counts.R script and the get_syn_nonSyn.py scripts into a single routine. 
6.	The file called get_syn_nonsyn.py is a script developed by Dr. Cornejo that obtains the synonymous and nonsynonymous sites from the alignments. 
7.	The remove_stop.sh file is a script developed by Dr. Cornejo that removed the stop codons from the alignments. 
8.	The run_orthofiner.sh file was utilized to obtain the total orthologous groups from the genome. 
9.	The transAlin.pl was the protein guided alignment in order to align the single copy orthologs. 
10.	The genes_under_selection.xlsx is the list of the top 5% of orthologous groups under selection. 
11.	The file called get_longest_protein.sh was the script developed by Dr. Cornejo to extract the longest protein from each of the orthogroups to perform annotation with Blast2Go. 
