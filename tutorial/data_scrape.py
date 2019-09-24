import sys
import os
import json

import physcraper
import dendropy
import pickle

from peyotl.nexson_syntax import (
    extract_tree,
    PhyloSchema,
)


configfi = "localaws.config"
study_id = "ot_350"
tree_id = "Tr53297"

#We will use an alignment deposited treebase
alnfile = "alignments/ot_350.aln"
assert os.path.isfile(alnfile) #check the file exists and the path is correct


workdir ="scrape_ot_350_trim"



# Read in the configuration information
conf = physcraper.ConfigObj(configfi)


#Get an existing tree from the Open Tree of life, and convert it to newick format
nexson = physcraper.opentree_helpers.get_nexson(study_id, 'api')
newick = extract_tree(nexson,
                      tree_id,
                      PhyloSchema('newick',
                                   output_nexml2json='1.2.1',
                                   content="tree",
                                   tip_label="ot:originalLabel"))

tre = dendropy.Tree.get(data=newick,
                        schema="newick",
                        preserve_underscores=True)



aln = dendropy.DnaCharacterMatrix.get(file=open(alnfile), schema="nexus", taxon_namespace=tre.taxon_namespace)


# To preserve taxon labels and relationships, 
#we will combine the alignement, tree and taxon information into a single data object
# By using the OpenTree Phylesystem API we can get the orgininal taxon names as well as the taxon mappings
data_obj = physcraper.generate_ATT_from_phylesystem(aln=aln,
                                         workdir=workdir,
                                         config_obj=conf,
                                         study_id=study_id,
                                         tree_id=tree_id)


sys.stdout.write("{} taxa in alignement and tree\n".format(len(data_obj.aln)))

## Note: often tre viewers cannot handle trees with multiple tips with the same label, 
#so write labelled has a default of "norepeats = True", and modifies the label to be unique
# alse write one out you can view in figtree etc
data_obj.write_labelled(label='^ot:ottTaxonName', filename="{}{}_original".format(study_id, tree_id))


# We need to create a physcraper ids object to translate between ncbi and OpenTree identifiers.
ids = physcraper.IdDicts(conf, workdir=workdir)


# Create an 'scraper' object that will link the blast results and the existing tree and taxa
scraper = physcraper.PhyscraperScrape(data_obj, ids)

# to get data from NCBI, align it and estimate a tree using RaxML
# This call wraps together a series of steps, including
## Blasting the sequences that are already in the alignment
# scraper.run_blast_wrapper()
## Reading in the new sequences, and dropping identical sequences
# scraper.read_blast_wrapper()
## Writing out the unaligned sequences
# scraper.write_all_unaligned()
## aligning the query seqs, and reading the alignemnt back in
# scraper.align_query_seqs()
## and then finally running Raxml on the new alignemnt, using the original tree as a strarting tree
## and reading that tree back into the scraper object
# You can run any set of these steps if you start from the beginning.

scraper.est_full_tree()

#write out the updated tree file, with taxon names as labels:
scraper.data.write_labelled(label='^ot:ottTaxonName', filename="{}{}_updated_norepeats".format(study_id, tree_id))

