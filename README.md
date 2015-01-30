#Elastic search#

Elastic search client that relies on:
* The official Elasticsearch toolkit: http://www.elasticsearch.org/
* The Python library to query ElasticSearch: https://github.com/elasticsearch/elasticsearch-py

It allows to start/stop automatically the ElasticSearch server and launch queries. It avoids to have multiple
instances of the ElasticSearch server running on the background.

##Installation##

The `install.sh` script will download and install all the required modules and packages.
1 git clone URL
2 cd URL
3 install.sh

##Usage##

Easy example of how to use this Python module:
```shell
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
```

This code can be found also in the script `example.py`, which you could run after the installation to check if everything is ok.
Basically you have to start the ElasticSearch engine (it will check if it's not already running), and then you can access to one
instance of the ElasticSearch client on `CelasticSearch().es`. At the end you can stop the server (only if you have launched it), or
leave it running for other processes to use it. API documentation for the object `CelasticSearch().es` can be found at http://elasticsearch-py.readthedocs.org/en/master/

##Contact##
* Ruben Izquierdo
* Vrije University of Amsterdam
* ruben.izquierdobevia@vu.nl  rubensanvi@gmail.com
* http://rubenizquierdobevia.com/
