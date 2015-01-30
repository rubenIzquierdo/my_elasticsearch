#!/usr/bin/env python

##############################################
# Author:   Ruben Izquierdo Bevia            # 
#           VU University of Amsterdam       #
# Mail:     ruben.izquierdobevia@vu.nl       #
#           rubensanvi@gmail.com             #
# Webpage:  http://rubenizquierdobevia.com   #
# Version:  1.0                              #
# Modified: 30-jan-2015                      #
##############################################

from my_elasticsearch import Celastic_search

my_es = Celastic_search()
print my_es.is_up()
my_es.start()

doc = {
    'author': 'Ruben',
    'text': 'Whatever you want to store',
}

res = my_es.es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['created'])
res = my_es.es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

my_es.stop()