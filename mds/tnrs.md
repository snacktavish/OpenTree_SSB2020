# Standardizing taxon names

One of the key challenges of comparing trees across studies is differences in taxon names because of spelling or taxonomic idiosincracies.

A solution to this, is mapping taxon names to unique identifiers using the Open Tree Taxonomic Name Resolution Service (TNRS). Theer are two options to use this service (bulk and API?). The names of the taxa you will search for this tutorial are saved in 'species_names.txt'

## Open Tree TNRS bulk upload tool.

Access this tool at https://tree.opentreeoflife.org/curator/tnrs/

This is a brand new beta-version of this functionality, so some parts are a bit finicky.

*Try this*
  * Click on "Add names..." (second button at the top of the menu on the left), and upload the names file `tutorial/species_names.txt`. The "loading file" window will not close by itself.
  * In the "Mapping options" section (bottom of the menu to the left):
    - select 'Animals' to narrow down the possibilities and speed up mapping
    - set it to replace '\_' with ' '
  * Click "Map selected names" (middle of the menu to the left).
  * Exact matches will show up in green, and can be accepted by clicking "accept exact matches".
  * A few taxa might still show several suggested names. Click through to the taxonomy, and select the one that you think is correct based on the phylogenetic context. (The tree is in the tutorial file as well if you want to double check).
  * Once you have accepted names for each of the taxa, click "Save nameset...", download it to your laptop, and extract (unzip) the files. You can take a look at the human readable version of the output at `output/main.csv`. `main.json` contains the the same data in a more computer readable format.
  * Finally, transfer the `main.json` file to the tutorial folder, so you can use it later for other cool analyses.

*Make sure your mappings were saved! If you do not **accept** matches (by clicking buttons), they do not download.*

For more on the OpenTree APIs see https://github.com/OpenTreeOfLife/germinator/wiki/Open-Tree-of-Life-Web-APIs




