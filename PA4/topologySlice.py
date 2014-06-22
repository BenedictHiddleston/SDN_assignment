'''
Coursera:
- Software Defined Networking (SDN) course
-- Network Virtualization

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
from collections import defaultdict

import pox.openflow.libopenflow_01 as of
import pox.openflow.discovery
import pox.openflow.spanning_tree

from pox.lib.revent import *
from pox.lib.util import dpid_to_str
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, EthAddr
from collections import namedtuple
import os

log = core.getLogger()


class TopologySlice (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Slicing Module")
        
        
    """This event will be raised each time a switch will connect to the controller"""
    def _handle_ConnectionUp(self, event):
        
        # Use dpid to differentiate between switches (datapath-id)
        # Each switch has its own flow table. As we'll see in this 
        # example we need to write different rules in different tables.
        dpid = dpidToStr(event.dpid)
        log.debug("Switch %s has come up.", dpid)
        
        """ Add your logic here """
        # s1
        if dpid == '00-00-00-00-00-01':

            # p3-p1
            m_131 = of.ofp_flow_mod()
            m_131.match.in_port = 3
            m_131.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(m_131)

            # p1-p3
            m_113 = of.ofp_flow_mod()
            m_113.match.in_port = 1
            m_113.actions.append(of.ofp_action_output(port = 3))
            event.connection.send(m_113)

            # p2-p4
            m_124 = of.ofp_flow_mod()
            m_124.match.in_port = 2
            m_124.actions.append(of.ofp_action_output(port = 4))
            event.connection.send(m_124)

            # p4-p2
            m_142 = of.ofp_flow_mod()
            m_142.match.in_port = 4
            m_142.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(m_142)


        elif dpid == '00-00-00-00-00-02':

            # p1-p2
            m_212 = of.ofp_flow_mod()
            m_212.match.in_port = 1
            m_212.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(m_212)

            # p2-p1
            m_221 = of.ofp_flow_mod()
            m_221.match.in_port = 2
            m_221.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(m_221)

        elif dpid == '00-00-00-00-00-03':

            # p1-p2
            m_312 = of.ofp_flow_mod()
            m_312.match.in_port = 1
            m_312.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(m_312)

            # p2-p1
            m_321 = of.ofp_flow_mod()
            m_321.match.in_port = 2
            m_321.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(m_321)


        elif dpid == '00-00-00-00-00-04':

            # p3-p1
            m_431 = of.ofp_flow_mod()
            m_431.match.in_port = 3
            m_431.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(m_431)

            # p1-p3
            m_413 = of.ofp_flow_mod()
            m_413.match.in_port = 1
            m_413.actions.append(of.ofp_action_output(port = 3))
            event.connection.send(m_413)

            # p2-p4
            m_424 = of.ofp_flow_mod()
            m_424.match.in_port = 2
            m_424.actions.append(of.ofp_action_output(port = 4))
            event.connection.send(m_424)

            # p4-p2
            m_442 = of.ofp_flow_mod()
            m_442.match.in_port = 4
            m_442.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(m_442)


        

        

def launch():
    # Run spanning tree so that we can deal with topologies with loops
    pox.openflow.discovery.launch()
    pox.openflow.spanning_tree.launch()

    '''
    Starting the Topology Slicing module
    '''
    core.registerNew(TopologySlice)
