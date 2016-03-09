# Working with the Gov-Info files

This directory contains iPython notebooks, WANE, and GML files which were used to work with a partial set of the Interent Archive for the parl.gc.ca domain.

The WANE files are a derived dataset containing extracted named entities and URLs.

The Python notebooks were developed to extract the named entities and URLs from the JSON in the WANEs and transform those items into a graph using the networkx Python module.

After transforming the files into a graph the graphs were saved using the GML file type for import into Gephi in order to visualize the graphs and perform eploratory data analysis.