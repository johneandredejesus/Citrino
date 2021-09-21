from datadefinition import Oper
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type


class CurrentThrottle(Oper):

    def __init__(self):
        """Current throttle details."""

        super().__init__('wd-oper:current-throttle')

class OverloadState(Oper):
    
    @force_type
    def __init__(self, current_throttle: CurrentThrottle = None):
        """Display overload control state."""

        super().__init__('wd-oper:overload-state')

        if is_not_none(current_throttle):
            self.append(current_throttle)

class MemoryState(Oper):

    def __init__(self):
        """Memory state."""

        super().__init__('wd-oper:memory-state')

class Configured(Oper):

    def __init__(self):
        """Memory configured by user."""

        super().__init__('wd-oper:configured')

class Memory(Oper):

    def __init__(self):
        """Memory information."""

        super().__init__('wd-oper:memory')

class ConfiguredMemory(Oper):

    def __init__(self):
        """Configured memory."""

        super().__init__('wd-oper:configured-memory')

class Default(Oper):
    
    @force_type
    def __init__(self, configured_memory: ConfiguredMemory = None, memory: Memory = None):
        """System default memory."""

        super().__init__('wd-oper:default')

        if is_not_none(configured_memory):
            self.append(configured_memory)
        
        if is_not_none(memory):
            self.append(memory)
        
class ThresholdMemory(Oper):
    
    @force_type
    def __init__(self, default: Default = None, configured: Configured = None):
        """Threshold memory."""

        super().__init__('wd-oper:threshold-memory')

        if is_not_none(default):
            self.append(default)
        
        if is_not_none(configured):
            self.append(configured)

class Node(Oper):
    
    @force_type
    def __init__(self, node_name: str, threshold_memory: ThresholdMemory = None, 
                       memory_state: MemoryState= None, overload_state: OverloadState = None):
        """node_name: str. Node ID."""

        super().__init__('wd-oper:node')

        if is_not_none(node_name):
            node_name_ = SubElement(self, 'wd-oper:node-name')
            node_name_.text = node_name
        
        if is_not_none(threshold_memory):
            self.append(threshold_memory)
        
        if is_not_none(memory_state):
            self.append(memory_state)

        if is_not_none(overload_state):
            self.append(overload_state)
        
class Nodes(Oper):

    def __init__(self):
        """List of nodes."""

        super().__init__('wd-oper:nodes')
    
    @force_type
    def node(self, value: Node):
        
        if is_not_none(value):
            self.append(value)

class WatchdogOper(Oper):
    
    @force_type
    def __init__(self, nodes: Nodes = None):
        """"
        module: Cisco-IOS-XR-wd-oper
        
        Watchdog information.
        """
        
        super().__init__('wd-oper:watchdog')

        self.set('xmlns:wd-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-wd-oper')

        if is_not_none(nodes):
            self.append(nodes)