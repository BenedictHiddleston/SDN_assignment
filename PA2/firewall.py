'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import csv



log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

''' Add your global variables here ... '''

block=[]

with open(policyFile) as f:
    reader = csv.reader(f,delimiter=',') 
  
    for row in reader:
        block.append(row[1:])

block.pop(0)


class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        ''' Add your logic here ... '''
        for row in block:
            # drop
            m = of.ofp_match()
            m.dl_src = EthAddr(row[0])
            m.dl_dst = EthAddr(row[1])
            
            # send to Openflow switch
            fm = of.ofp_flow_mod()
            fm.match = m
            event.connection.send(fm)
            
      
        

    
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
Starting the Firewall module
'''
    core.registerNew(Firewall)
