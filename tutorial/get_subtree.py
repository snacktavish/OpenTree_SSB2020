import os
from physcraper import opentree_helpers
from physcraper.treetaxon import TreeTax


json_file = "main.json"
citations_file = "cites.txt"
induced_subtree = "synth_subtree.tre"


#Use the bulk TNRS output to match your existing tree to standard labels
otu_dict = opentree_helpers.bulk_tnrs_load(json_file)

#Get the synthetic tree for the taxa in your estimated tree
ott_ids =set()
for otu in otu_dict:
   ott_ids.add(otu_dict[otu].get("^ot:ottId"))

#turn it back into a list
ott_ids = list(ott_ids)

tre = opentree_helpers.get_tree_from_synth(ott_ids=ott_ids, label_format="name", citation= citations_file)

# The synth tree doesn't have any branch lengths. That's generally fine, but some tree viewers want them!
# Lets set each branch length to 1
# Thanks Jeet Sukumaran and Dendropy for making this easy!!
for edge in tre.postorder_edge_iter():
    edge.length = 1.0


tre.write(path=induced_subtree,
          schema="newick",
          suppress_internal_taxon_labels=True,
          suppress_internal_node_labels=True)
