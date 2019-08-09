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


# Taxonomy Browser

[https://tree.opentreeoflife.org/taxonomy/browse](https://tree.opentreeoflife.org/taxonomy/browse?id=93302) is our browser for the Open Tree Taxonomy.
That taxonomy is an input into our full synthetic tree and
is used to help us align tips in different trees that refer to the same taxon.

The taxonomy includes links to unique identifiers in other digitally available taxonomies, such as GBIF or NCBI.


### Accessing data using the website
Check out https://tree.opentreeoflife.org

Search for your favorite organism!
Don't agree with the relationships? Never fear! We'll see how to fix them by uploading new inferences.


You can use the download a subtree of interest directly from the website.


## Getting an induced subtree

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

(This is a brand new beta-versionof teh site, some parts are a bit finicky).

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
curl -X POST https://api.opentreeoflife.org/v3/tree_of_life/induced_subtree -H "content-type:application/json" -d '{"ott_ids":[292466, 267845, 666104, 316878, 102710]}'
```
For more on the OpenTree APIs see https://github.com/OpenTreeOfLife/germinator/wiki/Open-Tree-of-Life-Web-APIs


Is often more convenient to manipulate both trees and names within a scripting language.

We will use wrappers available in the python packages Physcraper and Peyotl to make it easier to work with the Open Tree Api's

They are already installed on the cluster, in a python virtual environment.

To run these analyses on the cluster, activate the python virtual environment
```
source /class/molevol-software/venv-physcraper/bin/activate

```

To install on your own laptop see:
```
https://github.com/McTavishLab/physcraper/blob/master/INSTALL
```


Your terminal should show **(venv-physcraper)** to the left of the bash prompt.



----------------------------------------------------


Say we wanted to get some more taxonomic context for our inferences that we made
using IQ Tree? How does that tree (which we know is contentious) compare to taxonomy and other published literature?



We could go to https://tree.opentreeoflife.org/taxonomy/browse

Or we can do queries directly via the command lineages

The family that penguins are is is named "Spheniscidae"

```
curl -X POST https://api.opentreeoflife.org/v3/tnrs/match_names \
-H "content-type:application/json" -d \
'{"names":["Spheniscidae"]}'
```

From that output, we can get the OpenTree taxon ID for penguins.

It is 494367.

We can get the full taxonomic subtree for that taxon.

```
curl -X POST https://api.opentreeoflife.org/v3/taxonomy/subtree \
-H 'Content-type:application/json' -d '{"ott_id":494367}'
```

Gallus gallus
Crocodylus niloticus


```
curl -X POST https://api.opentreeoflife.org/v3/tree_of_life/induced_subtree -H "content-type:application/json" -d '{"ott_ids":[292466, 267845, 666104, 316878, 102710]}'
```

## Alternative approaches (optional)
##### Using R/ Rstudio
We won't use R today, but there is a great package, [Rotl](https://github.com/ropensci/rotl) that makes it easy to access and work with OpenTree data in R.


Tutorial on rotl at : https://ropensci.org/tutorials/rotl_tutorial/
Tutorial on linking data from OpenTree with species locations from GBIF:
https://mctavishlab.github.io/BIO144/labs/rotl-rgbif.html



## Updating inferences with new data
### Gene sequence data





### Genomic data
One of the key challenges of phylogenetic inferences using genomic data is assessing homology.

One approach we have been using is mapping new reads directly to existing inferences,
but this approach is work in progress.
https://github.com/McTavishLab/phycorder/tree/offbyone_dev
