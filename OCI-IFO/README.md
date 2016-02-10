# OCI-IFO (Observatoire de l'information - Information Flow Observatory)

The Information Flow Observatory is a research group dedicated to media studies (http://www.oci-ifo.org). As part of our work we are building a system that scrapes news from all over Canada. We are also involved in data visualization and critical analysis of the information. One of our goal is to share tools, data and research findings. Hope you'll have fun playing with these! 

##What you'll find here:

* Since January 26th 2016, I have have been scraping news from Canadian media web sites, not all of them but a few hundreds.
* News items are stored in a MongoDB database and this dataset is made available to all participants.
* To get you started with the dataset, I'm providing basic ready-to-use python and php scripts.

### for the python fans

* Requirements:
 * Python! (tested on 2.7)
 * pymongo (sudo pip install pymongo) on ubuntu

* Instructions (tested on ubuntu)
 * Download the scripts
 * using a terminal go to the folder where files have been downloaded (cd /path/to/folder/)
 * type : python name_of_script.py

The output will show up in your terminal. To write the output to a file, edit the script and uncomment the lines "save output to file".
Feel free to modify the queries as you wish. You may want to check out the folder "data_samples" in order to understand how the database is structured.

### for the php fans

* Requirements
 * a web server (tested on Apache)
 * PHP (tested on 5.5.9)
 * mongodb php driver (https://docs.mongodb.org/ecosystem/drivers/php/)

* Instructions
 * download the script to your web server
 * type in the url http://yourwebserver.com/path/to/file/articles_by_keywords.php
 * The output is a valid JSON file

Optionally, you may try this script live on our server at http://www.oci-ifo.org/oci_php_scripts/articles_by_keywords.php. You may also copy the output to http://jsonviewer.stack.hu/. It provides a nice tool that makes it easy to visualize JSON data.

Again, feel free to modify the queries as you wish. You may want to check out the folder "data_samples" in order to understand how the database is structured.
 




