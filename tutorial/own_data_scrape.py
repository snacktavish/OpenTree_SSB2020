import sys
import os
import json
import dendropy
import pickle
from peyotl.nexson_syntax import (
    extract_tree,
    PhyloSchema,
)

import physcraper
from physcraper import opentree_helpers
from physcraper.aligntreetax import generate_ATT_from_files


configfi = "aws.config"
workdir ="own_data"


alnfi = "physcraper/tests/data/tiny_test_example/test.fas"
mattype ="fasta"
treefi = "physcraper/tests/data/tiny_test_example/test.tre"
schema_trf = "newick"


## What taxon do you want to include new seqs from? Search for it on Open Tree, and se the id here:
## This is genus Senecio

ingroup_mrca ='18794'


## input mappings from your labels to OpenTree, via bulk TNRS
bulk_names_json = 'physcraper/tests/data/tiny_test_example/main.json'
otu_dict = opentree_helpers.bulk_tnrs_load(bulk_names_json)


## Need to write them to a file for the ATT from file load

if not os.path.exists(workdir):
    os.makedirs(workdir)

otu_jsonfi = "{}/otu_dict_input.json".format(workdir)
with open(otu_jsonfi, 'w') as outfi:
    outfi.write(json.dumps(otu_dict))


# Read in the configuration information
conf = physcraper.ConfigObj(configfi)

## Create a unified AlignmentTreeTaxon object from these files
data_obj =  generate_ATT_from_files(seqaln=alnfi,
                                    mattype=mattype,
                                    workdir=workdir,
                                    config_obj=conf,
                                    treefile=treefi,
                                    schema_trf=schema_trf,
                                    otu_json=otu_jsonfi,
                                    ingroup_mrca=ingroup_mrca)


sys.stdout.write("{} taxa in alignement and tree\n".format(len(data_obj.aln)))

## Note: often tre viewers cannot handle trees with multiple tips with the same label, 
#so write labelled has a default of "norepeats = True", and modifies the label to be unique
# alse write one out you can view in figtree etc
data_obj.write_labelled(label='^ot:ottTaxonName', filename="original")


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
scraper.data.write_labelled(label='^ot:ottTaxonName', filename="updated")


