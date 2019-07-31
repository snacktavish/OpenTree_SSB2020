a
---
title: "Sample Document"
output: html_document
bibliography: bibliography.bib
---

# Updating and visualizing phylogenetic trees


There any many ways to generate phylogenetic trees!  
All kinds of data, lots of analysis methods.
We've talked a lot about estimating trees. But what do we do with them?

**How can we contextualize our phylogenetic inferences in the context of existing literature and taxonomy?**

One of the key challenges of comparing tree across studies is minor differences in names and naming.

In this tutorial we will walk through:
  * Standardizing names of our inferences
  * Getting a tree for comparisons
  * Updating an existing phylogeny with new data from GenBank
  * Making comparisons between our trees and existing phylogenetic inferences and taxonomy.


# The Open Tree of Life
The Open Tree of Life (https://opentreeoflife.github.io/) is a project that unties phylogenetic inferences and taxonomy to provide a synthetic estimate of species relationships across the entire tree of life.
![](otol_logo.png)  


This tree currently includes 2.7 million tips.
65,000 of these taxa have relationships inferred from phylogeny.

The synthetic tree uses a combined taxonomy across a large number of taxonomy resources with evolutionary estimates from published phylogenetic studies.
https://opentreeoflife.github.io/browse/



# Tree Browser

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

The properities panel contains:

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


### Accessing data using the website
Check out https://tree.opentreeoflife.org

Search for your favorite organism!
Don't agree with the relationships? Never fear! We'll see how to fix them by uploading new inferences.


You can use the download a subtree of interest directly from the website.


### Using API's



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
