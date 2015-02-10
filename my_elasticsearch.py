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

import os
import sys
import signal
import time
import logging
from subprocess import Popen, PIPE
from libs import elasticsearch

SUBPATH_TO_ES=os.path.join('libs','elasticsearch','bin','elasticsearch')

class Celastic_search:
    def __init__(self):
        self.create_logger()
        self.here = os.path.dirname(os.path.realpath(__file__))
        self.es = elasticsearch.Elasticsearch()
        self.pid_process_elasticsearch = None
        if not self.is_up():
            self.start()
        
    def create_logger(self):
        self.logger = logging.getLogger(__file__)
    
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        
    def is_up(self):
        return self.es.ping()
    
    def start(self):
        if not self.is_up():
            whole_path_es = os.path.join(self.here,SUBPATH_TO_ES)
            es_proc = Popen(whole_path_es, stdout=PIPE, stderr=PIPE,stdin=PIPE)
            self.pid_process_elasticsearch = es_proc.pid
            self.logger.info('Starting Elastic search with pid %s' % self.pid_process_elasticsearch)
            while not self.is_up():
                time.sleep(1)
        else:
            self.logger.info('Elastic search is already running')
            
    def stop(self):
        if self.pid_process_elasticsearch is not None:
            os.kill(self.pid_process_elasticsearch, signal.SIGKILL)
            self.logger.info('Stopping Elastic search with pid %s' % self.pid_process_elasticsearch)
        else:
            self.logger.info('This client did not launch ElasticSearch and can not stop it')
            
            
    def index_exists(self,idx_name):
        '''
        Checks if the given index exists or not
        '''
        return self.es.indices.exists(idx_name)
    
    def create_index(self,idx_name):
        '''
        Create the given index
        '''
        self.es.indices.create(index=idx_name)
        
    def search_exists(self, my_index, my_doc_type, dsl_query):
        exists = False
        try:
            res = self.es.search_exists(index = my_index, doc_type=my_doc_type, body = dsl_query)
            exists = res['exists']
        except:
            exists = False
        return exists
    
    def search(self, my_index, my_doc_type, dsl_query):
        res = None
        try:
            res = self.es.search(index = my_index, doc_type=my_doc_type, body = dsl_query)
        except:
            res = None
        return res
    
    def index_document(self, my_index, my_doc_type, dsl_doc):
        res = None
        try:
            res = self.es.index(index=my_index, doc_type = my_doc_type, body = dsl_doc)
        except:
            res = None
        return res
            
    
                 
        
        
        

        
    