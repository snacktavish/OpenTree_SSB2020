# Standardizing taxon names

The names of the taxa you will search for are saved in
'species_names.txt'


One of the key challenges of comparing trees across studies is minor differences in names and naming.
We will map them to unique identifiers using the Open Tree TNRS bulk upload tool https://tree.opentreeoflife.org/curator/tnrs/

(This is a brand new beta-version of this functionality, so some parts are a bit finicky).

*Try this*
  * Click on "add names", and upload the names file. (tutorial/species_names.txt)
  * In the mapping options section,
    - select 'animals' to narrow down the possibilities and speed up mapping
    - set it to replace '\_' with ' '
  * Click "Map selected names"

Exact matches will show up in green, and can be accepted by clicking "accept exact matches".

A few taxa still show several suggested names. Click through to the taxonomy, and select the one that you think is correct based on the phylogenetic context. (The tree is in the tutorial file as well if you want to double check).

Once you have accepted names for each of the taxa, click "save nameset".

Download it to your laptop.
Extract the files.
Take a look at the human readable version (output/main.csv).

*Make sure your mappings were saved! If you don't 'accept' matches, they don't download.*

main.json contains the the same data in a more computer readable format.
Transfer the main.json file to the tutorial folder on the cluster.

### Using API's
You can use the OpenTree API's to get the tree for a subset of taxa directly from the command line

For example:
```
curl -X POST https://api.opentreeoflife.org/v3/tree_of_life/induced_subtree -H "content-type:application/json" -d '{"ott_ids":[292466, 267845, 316878]}'
```
For more on the OpenTree APIs see https://github.com/OpenTreeOfLife/germinator/wiki/Open-Tree-of-Life-Web-APIs


It is often more convenient to manipulate both trees and names within a scripting language.


### Using Python
We will use wrappers available in the python packages Physcraper and Peyotl to make it easier to work with the Open Tree Api's

They are already installed on the cluster, in a python virtual environment.

To run these analyses on the cluster, activate the python virtual environment (this loads the installed modules)
```
source /class/molevol-software/venv-physcraper/bin/activate

```

To install and run on your own laptop see the instructions on https://github.com/McTavishLab/physcraper/blob/master/INSTALL

Your terminal should show **(venv-physcraper)** to the left of the bash prompt.
