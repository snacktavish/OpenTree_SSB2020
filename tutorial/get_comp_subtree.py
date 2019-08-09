import os
from physcraper import opentree_helpers
from physcraper.treetaxon import TreeTax


json_file = "main.json"

estimated_tree = "turtle_iqtree.tre"
estimated_tree_OTT = "turtle_iqtree_OTT.tre"
induced_subtree = "synth_turtles.tre"

#citations_file = "tutorial/cites.txt"


#Use the bulk TNRS output to match your existing tree to standard labels
tt = TreeTax(otu_json=json_file, treefrom=estimated_tree)

#Use write out your tree with standard labels
tt.write_labelled(estimated_tree_OTT, label = "^ot:ottTaxonName", norepeats=False)


#Get the synthetic tree for the taxa in your estimated tree
ott_ids =set()
for otu in tt.otu_dict:
   ott_ids.add(tt.otu_dict[otu].get("^ot:ottId"))

#turn it back into a list
ott_ids = list(ott_ids)

tre = opentree_helpers.get_tree_from_synth(ott_ids=ott_ids, label_format="name")
tre.write(path=induced_subtree,
          schema="newick",
          suppress_internal_taxon_labels=True,
          suppress_internal_node_labels=True,
          preserve_underscores=False)
