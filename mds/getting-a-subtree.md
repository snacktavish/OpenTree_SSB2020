# Getting a subtree for your taxa

It is often more useful to access a pruned subtree for just the taxa you are interested in.
In order to do so, you need to map taxon names to unique identifiers. If you have not done that check the section [Standardizing taxon names](mds/tnrs.html) before continuing.

If your name have been standardise to Open Tree of Life's taxonomy, go on and take a look at the script in the tutorials folder 'get_subtree.py'.
This script gets the OpenTree ids from your taxonomy mapping file 'main.json',
and uses them to get a tree for those taxa.

Edit the location of your json file, and run get subtree.py
```
    $ python get_subtree.py
```

It will write two files out to your current working directory - the tree, 'synth_subtree.tre' and the citations of published trees that went into generating that tree, and support the relationships in it.

Move both those files to your computer.
Open the synthetic subtree in figtree to look at the placement of turtles.
