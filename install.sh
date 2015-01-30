#!/bin/bash

##############################################
# Author:   Ruben Izquierdo Bevia            # 
#           VU University of Amsterdam       #
# Mail:     ruben.izquierdobevia@vu.nl       #
#           rubensanvi@gmail.com             #
# Webpage:  http://rubenizquierdobevia.com   #
# Version:  1.0                              #
# Modified: 30-jan-2015                      #
##############################################

here=$(pwd)
rm -rf libs 2> /dev/null
mkdir libs

###############################################
# Elastic search
###############################################
cd libs
wget --no-check-certificate https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.zip
unzip elasticsearch-1.4.2.zip
rm elasticsearch-1.4.2.zip
ln -s elasticsearch-1.4.2 elasticsearch
cd ..
###############################################
# Elastic search py
###############################################
cd libs
git clone https://github.com/elasticsearch/elasticsearch-py
mv elasticsearch-py elasticsearchPy
cd elasticsearchPy
touch __init__.py
cd ..
echo "from elasticsearchPy import elasticsearch" >> __init__.py
cd ..


