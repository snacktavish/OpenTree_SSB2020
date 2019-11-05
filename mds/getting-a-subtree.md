# Getting a subtree for your taxa

It is often more useful to access a pruned subtree for just the taxa you are interested in.
In order to do so, you need to map taxon names to unique identifiers. If you have not done that check the section [standardizing taxon names](mds/tnrs.md) before continuing.

If your name have been standardise to Open Tree of Life's taxonomy, you can get a subtree in two different ways.

## Get a subtree using API's
You can use the OpenTree API's to get the tree for a subset of taxa directly from the command line

For example:
```
curl -X POST https://api.opentreeoflife.org/v3/tree_of_life/induced_subtree -H "content-type:application/json" -d '{"ott_ids":[292466, 267845, 316878]}'
```

It is often more convenient to manipulate both trees and names within a scripting language. For that, we will use Python.

## Get a subtree using Python
<!--We will use wrappers developed in the python packages Physcraper and Peyotl to make it easier to work with the Open Tree Api's

They are already installed on the cluster, in a python virtual environment.

To run these analyses on the cluster, activate the python virtual environment (this loads the installed modules)
```
source /class/molevol-software/venv-physcraper/bin/activate

```

To install and run on your own laptop see the instructions on https://github.com/McTavishLab/physcraper/blob/master/INSTALL

-->

If you have a physcraper vurtual environment do `source venv-physcraper/bin/activate`. If not follow the instructions to set it up in [LINK TO INSTALL AS .MD FILE!](https://github.com/McTavishLab/physcraper/blob/master/INSTALL.md)

*If your virtual environment has installed properly, your terminal should show `(venv-physcraper)` to the left of the bash prompt.*

Now, take a look at the script in the tutorials folder 'get_subtree.py'.
This script gets the OpenTree ids from your taxonomy mapping file 'main.json',
and uses them to get a tree for those taxa.

Edit the location of your json file if needed, and run get subtree.py
```
    $ python get_subtree.py
```

It will write two files out to your current working directory - the tree as 'synth_subtree.tre', and the citations of published trees that went into generating that tree, and that support the relationships in it.

Move both those files to your computer.
Open the synthetic subtree in figtree to look at the placement of turtles.

