---
title: "Comparing and updating phylogenetic trees"
output: html_document
bibliography: bibliography.bib
---

# Comparing and updating phylogenetic trees


There any many ways to generate phylogenetic trees!  
All kinds of data, lots of analysis methods.
We've talked a lot about estimating trees. But what do we do with them?

**How can we contextualize our phylogenetic inferences in existing literature and taxonomy?**

One of the key challenges of comparing tree across studies is minor differences in names and naming.

In this tutorial we will walk through:
  * Standardizing taxon names
  * Getting existing trees for arbitrary sets of taxa
  * Visualizing conflict between estimates
  * Updating an existing phylogeny with new data from GenBank


# The Open Tree of Life
The Open Tree of Life (https://opentreeoflife.github.io/) is a project that unties phylogenetic inferences and taxonomy to provide a synthetic estimate of species relationships across the entire tree of life.  
![](otol_logo.png)  


This tree currently includes 2.7 million tips.
65,000 of these taxa have relationships inferred from phylogeny.

The synthetic tree uses a combined taxonomy across a large number of taxonomy resources with evolutionary estimates from published phylogenetic studies.
https://opentreeoflife.github.io/browse/


## The synthetic tree


## Tree Browser

[https://tree.opentreeoflife.org](https://tree.opentreeoflife.org)
is our interactive tree viewer.
You can browse by  the synthetic tree and leave feedback.

### Navigation

Click on nodes to move through the tree.
If you click the "Legend" button at the top, you will get an explanation
    of what information the visual elements of the tree convey.

### Seeing more info about a node

You can reveal the "Properties panel" by clicking on "**ⓘ** Show Properties"
    button or the "**ⓘ**" link that appears when your mouse is over a node or
    branch in the tree.

The properties panel contains:

  * links to the taxon in our reference taxonomy (OTT) and other taxonomies
  * the ID of the node
  * the count of how many tips in the tree descend from the node
  * information about how to download a Newick representation of the subtree
      rooted at that node, and
  * information about taxonomies and phylogenies that support or disagree with
    that node.

Clicking on "**ⓘ** Hide Properties" will hide the panel so that you can see more
    of the tree.

### Feedback

If you have feedback about the relationships that you see, use the "Add Comment" button.
Comments that are entered here are stored as issues in our
[feedback repository](https://github.com/OpenTreeOfLife/feedback/issues).


## Taxonomy Browser

[https://tree.opentreeoflife.org/taxonomy/browse](https://tree.opentreeoflife.org/taxonomy/browse?id=93302) is our browser for the Open Tree Taxonomy.
That taxonomy is an input into our full synthetic tree and
is used to help us align tips in different trees that refer to the same taxon.

The taxonomy includes links to unique identifiers in other digitally available taxonomies, such as GBIF or NCBI.


## Accessing data using the website
Check out https://tree.opentreeoflife.org

Search for your favorite organism!
Don't agree with the relationships? Never fear! We'll see how to fix them by uploading new inferences.


You can use the download a subtree of interest directly from the website.


## Getting a tree for your taxa

It is often more useful to access the pruned subtree for just the taxa you are interested in.
In order to do so, you need to map taxon names to unique identifiers.

Get the tutorial folder using
```
    git clone https://github.com/snacktavish/Mole2019.git
    cd  WH2019/tutorial
```

The names of the taxa you included used in your tree estimation in Minh's lab are in the file
'species_names.txt'


We will map them to unique identifiers using the Open Tree TNRS bulk upload tool https://tree.opentreeoflife.org/curator/tnrs/

(This is a brand new beta-versionof the site, some parts are a bit finicky).

  * Click on "add names", and upload the names file. (tutorial/species_names.txt)  
  * In the mapping options section,
    - select 'animals' to narrow down the possibilities and speed up mapping
    - set it to replace '\_' with ' '
  * Click "Map selected names"

Exact matches will show up in green, and can be accepted by clicking "accept exact matches".

A few taxa still show several suggested names. Click through to the taxonomy, and select the one that you think is correct based on the phylogenetic context. (The tree is in the tutorial file as well if you want to double check).

Once you have accepted names for each of the taxa, click "save nameset".

Download it to your laptop.
Extract the file.
Take a look at the human readable version (main.csv) and transfer the main.json file to the tutorial folder on the cluster.

### Using API's
You can use the OpenTree API's to get the tree for a subset of taxa directly from the command line


For example:
```
curl -X POST https://api.opentreeoflife.org/v3/tree_of_life/induced_subtree -H "content-type:application/json" -d '{"ott_ids":[292466, 267845, 666104, 316878]}'
```
For more on the OpenTree APIs see https://github.com/OpenTreeOfLife/germinator/wiki/Open-Tree-of-Life-Web-APIs


Is often more convenient to manipulate both trees and names within a scripting language.

### Using R/ Rstudio  (optional)
We won't use R today, but there is a great package, [Rotl](https://github.com/ropensci/rotl) that makes it easy to access and work with OpenTree data in R.


Tutorial on rotl at : https://ropensci.org/tutorials/rotl_tutorial/
Tutorial on linking data from OpenTree with species locations from GBIF:
https://mctavishlab.github.io/BIO144/labs/rotl-rgbif.html


### Using Python
We will use wrappers available in the python packages Physcraper and Peyotl to make it easier to work with the Open Tree Api's

They are already installed on the cluster, in a python virtual environment.

To run these analyses on the cluster, activate the python virtual environment (this loads the installed modules)
```
source /class/molevol-software/venv-physcraper/bin/activate

```

To install and run on your own laptop see:
```
https://github.com/McTavishLab/physcraper/blob/master/INSTALL
```

Your terminal should show **(venv-physcraper)** to the left of the bash prompt.


Take a look at the script in the tutorials folder 'get_subtree.py'.
This script gets the OpenTree ids from your taxonomy mapping file 'main.json',
and uses them to get a tree for those taxa.

Edit the location of your json file, and run get subtree.py

    $ python get_subtree.py
It will write two files out to your current working directory - the tree, 'synth_subtree.tre' and the citations of published trees that went into generating that tree, and support the relationships in it.

Move both those files to your computer.
Open the synthetic subtree in figtree.

## Comparing trees
Say we wanted to get some more taxonomic context for our inferences that we made
using IQ Tree? How does that tree (which we know is contentious) compare to taxonomy and other published literature?

In order to make comparisons about statements that two different trees are making about the same set of taxa, we need to make sure the labels on the tree match.

We will use our same taxonomy mapping file to match the tips of our estimated tree to the standardized labels in Open Tree.

Open 'tutorial/rename_tips.py'.

This is a very simple script that takes your mapped labels, and uses the conversion from 'original name' to replace the tip names on your tree with the standardized names

Run this file. If you want to, replace the path to my turtle tree ('turtle_iqtree.tre') estimate with the one you estimated in Minh's lab

  $ python rename_tips.py

This should generate file labelled 'turtle_iqtree_OTT.tre'

Transfer this file to your computer.

### Using Phylo.io to compare two trees
A quick way to visualize even fairly large trees is
http://phylo.io/

If you have trees with matching labels, you can do a quick comparison.

Upload both trees to phylo.io

Is your tree inference different that the relationships from OpenTree?

How so?


### Uploading your own tree to OpenTree for interactive comparison with the OpenTree synthetic tree and Taxonomy

When experimenting with OpenTree, or doing demo's **please** use our development site,
https://devtree.opentreeoflife.org/curator
There will be a red banner in the corner!

I will demonstrate how to upload your inference tree to OpenTree using the curator sites,
but if you want to try it out yourself later, there are detailed instructions at:
https://github.com/OpenTreeOfLife/opentree/wiki/Submitting-phylogenies-to-Open-Tree-of-Life



## Automated updating of an existing tree
There is a lot of sequence data that has been generated, but has never been incorporated into any phylogenetic estimates.
We only store phylogenies and associated metadata in OpenTree, not alignments.

## Updating gene trees
However, if you have access to a single gene alignment, and a tree, you can automate adding homologous data into your tree by searching NCBI.

These automated tree can provide a quick inference or potential relationships, of problems in the taxonomic assignments of sequences, and flag areas of potential systematic interest.

By using a starting tree and alignement, Physcraper, takes advantage of loci that previous researchers have assessed and deemed appropriate for the problem at hand.

In order to minimize the risk of incorrectly assigning homology, tips in the starting tree are mapped to the Open Tree taxonomy, as above, and only adding new sequences that are within that ingroup.

We'll walk through the script 'data_scrape.py' together, and then run it.

  $ python data_scrape.py



### Genomic data (not part of tutorial)
One of the key challenges of phylogenetic inferences using genomic data is assessing homology.

One approach we have been using is mapping new reads directly to existing inferences,
but this approach is work in progress.
https://github.com/McTavishLab/phycorder/tree/offbyone_dev
While we are working on applying these techniques to genome scale alignements (Work in progress at https://github.com/McTavishLab/phycorder)


## On your own!
#### Choose your own adventure.

## Get Synth tree
Make a list of taxa of your own and save it in a text file.

Scientific names only.

Resolve those names to Open Tree identifiers, and modify get_tree.py to get a tree for our taxa of interest.


Do you have a published tree that would do a better job on those relationships, but it isn't included in the synthetic tree?

Upload it to the production site tree.opentreeoflife.org


## Update a different tree

Choose differnet tree that has data in treebase, or that you have your own (single gene) alignment for!
Modify

$ python data_scrape_alt.py

to try to scrape data for those taxa.
%TODO (set of suggested pairs that have worked)
%TDOD Script for OwnFile

Upload your extended tree to devtree.opentreeoflife.org/curator

(requires a github login)


## Zoom around

Brain a bit tired? Check out some fun visualizations of the OpenTree tree.

Take a look at OneZoom https://www.onezoom.org/ tree of life explorer

or this hyperbolic tree https://glouwa.github.io/


---
