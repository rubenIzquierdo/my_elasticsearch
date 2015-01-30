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
from subprocess import Popen, PIPE
from libs import elasticsearch

SUBPATH_TO_ES=os.path.join('libs','elasticsearch','bin','elasticsearch')

class Celastic_search:
    def __init__(self):
        self.here = os.path.dirname(os.path.realpath(__file__))
        self.es = elasticsearch.Elasticsearch()
        self.pid_process_elasticsearch = None
        
    def is_up(self):
        return self.es.ping()
    
    def start(self):
        if not self.is_up():
            whole_path_es = os.path.join(self.here,SUBPATH_TO_ES)
            es_proc = Popen(whole_path_es, stdout=PIPE, stderr=PIPE,stdin=PIPE)
            self.pid_process_elasticsearch = es_proc.pid
            print>>sys.stderr,'Running ES with pid', self.pid_process_elasticsearch
            while not self.is_up():
                time.sleep(1)
        else:
            print>>sys.stderr,'Elastic search is already running'
            
    def stop(self):
        if self.pid_process_elasticsearch is not None:
            os.kill(self.pid_process_elasticsearch, signal.SIGKILL)

            print>>sys.stderr,'Kill process', self.pid_process_elasticsearch
        else:
            print>>sys.stderr,'This object did not launch ElasticSearch and can not stop it'
            
    
                 
        
        
        

        
    