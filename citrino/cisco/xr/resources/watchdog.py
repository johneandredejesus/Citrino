from datadefinition import OperationEnum, Cfg
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type


class  ThresholdMemory(Cfg):
    
    @force_type
    def __init__(self, minor: int = None, severe: int = None, critical: int = None, operation: OperationEnum.Operation = None):
        """
        Memory thresholds.

        minor: int: range "5..40". Threshold, Range (5, 40).

        severe: int: range "4..40". Threshold, Range (4, minor).
        
        value: int: range "3..40". Threshold, Range (3, severe).
        """

        super().__init__('watchd-cfg:threshold-memory')
        
        minor_ = SubElement(self, 'watchd-cfg:minor')

        if is_not_none(minor):
            minor_.text = convert_to_string(minor)
        
        severe_ = SubElement(self, 'watchd-cfg:severe')

        if is_not_none(severe):
            severe_.text = convert_to_string(severe)
        
        critical_ = SubElement(self, 'watchd-cfg:critical')

        if is_not_none(critical):
            critical_.text = convert_to_string(critical)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)
        


class  DiskLimit(Cfg):
    
    @force_type
    def __init__(self, minor: int = None, severe: int = None, critical: int = None, operation: OperationEnum.Operation = None):
        """
        Disk thresholds.

        minor: int: range "5..40". Threshold, Range (5, 40).
        
        severe: int: range "4..40". Threshold, Range (4, minor).
        
        critical: int: range "3..40". Threshold, Range (3, severe).
        """

        super().__init__('watchd-cfg:disk-limit')
        
        minor_ = SubElement(self, 'watchd-cfg:minor')

        if is_not_none(minor):
            minor_.text = convert_to_string(minor)
        
        severe_ = SubElement(self, 'watchd-cfg:severe')

        if is_not_none(severe):
            severe_.text = convert_to_string(severe)
        
        critical_ = SubElement(self, 'watchd-cfg:critical')

        if is_not_none(critical):
            critical_.text = convert_to_string(critical)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)
               

class WatchdBase(Cfg):
    
    @force_type
    def __init__(self, module_name: str):

        """module: Cisco-IOS-XR-watchd-cfg."""

        super().__init__(module_name)

        self.set('xmlns:watchd-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-watchd-cfg')


class WatchdogCfg(WatchdBase):
    
    @force_type
    def __init__(self, threshold_memory: ThresholdMemory = None, disk_limit: DiskLimit = None):
        """
        module: Cisco-IOS-XR-watchd-cfg.

        Watchdog configuration commands.
        """

        super().__init__('watchd-cfg:watchdog')
        
        if is_not_none(threshold_memory):
            self.append(threshold_memory)
        
        if is_not_none(disk_limit):
            self.append(disk_limit)
    
    @force_type
    def overload_notification(self, operation: OperationEnum.Operation = None):
        """
        Disable critical event notification.
        """

        overload_notification_ = SubElement(self, 'watchd-cfg:overload-notification')

        if is_not_none(operation):
            overload_notification_.set('xc:operation', operation.value)
    
    @force_type
    def restart_deadlock_disable(self, operation: OperationEnum.Operation = None):
        """
        Disable watchdog restart memory-hog.
        """

        restart_deadlock_disable_ = SubElement(self, 'watchd-cfg:restart-deadlock-disable')

        if is_not_none(operation):
            restart_deadlock_disable_.set('xc:operation', operation.value)
    
    @force_type
    def restart_memoryhog_disable(self, operation: OperationEnum.Operation = None):
        """
        Disable watchdog restart memory-hog.
        """

        restart_memoryhog_disable_ = SubElement(self, 'watchd-cfg:restart-memoryhog-disable')

        if is_not_none(operation):
            restart_memoryhog_disable_.set('xc:operation', operation.value)
    
    @force_type
    def overload_throttle_timeout(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Watchdog overload throttle timeout configuration.
        
        units "second".

        value: int: range "5..120".
        """

        overload_throttle_timeout_ = SubElement(self, 'watchd-cfg:overload-throttle-timeout')
        
        if is_not_none(value):
            overload_throttle_timeout_.text = convert_to_string(value)

        if is_not_none(operation):
            overload_throttle_timeout_.set('xc:operation', operation.value)


class WatchdCfg(WatchdBase):

    def __init__(self):
        """"
        module: Cisco-IOS-XR-watchd-cfg.
        
        watchd.
        """

        super().__init__('watchd-cfg:watchd')
    
    @force_type
    def timeout(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Length of timeout in seconds.
        
        units "second".

        value: int: range "1..10".
        """

        timeout_ = SubElement(self, 'watchd-cfg:timeout')

        if is_not_none(value):
            timeout_.text = convert_to_string(value)
        
        if is_not_none(operation):
            timeout_.set('xc:operation', operation.value)


class DiskThreshold(Cfg):
    
    @force_type
    def __init__(self, minor: int = None, severe: int = None, critical: int = None, operation: OperationEnum.Operation = None):
        """
        Disk thresholds.

        minor: int: range "5..40". Threshold, Range(5, 40).

        severe: int: range "4..40". Threshold, Range(4, minor). 

        critical: int: range "3..40". Threshold, Range(3, severe).
        """

        super().__init__('watchd-cfg:disk-threshold')
        
        minor_ = SubElement(self, 'watchd-cfg:minor')

        if is_not_none(minor):
            minor_.text = convert_to_string(minor)
        
        severe_ = SubElement(self, 'watchd-cfg:severe')

        if is_not_none(severe):
            severe_.text = convert_to_string(severe)
        
        critical_ = SubElement(self, 'watchd-cfg:critical')

        if is_not_none(critical):
            critical_.text = convert_to_string(critical)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)
           

class MemoryThreshold(Cfg):
    
    @force_type
    def __init__(self, minor: int = None, severe: int = None, critical: int = None, operation: OperationEnum.Operation = None):
        """
        Memory thresholds.
        
        minor: int: range "5..40". Threshold, Range(5, 40).

        severe: int: range "4..40". Threshold, Range(4, minor).

        critical: int: range "3..40". Threshold, Range(3, severe).
        """

        super().__init__('watchd-cfg:memory-threshold')

        minor_ = SubElement(self, 'watchd-cfg:minor')

        if is_not_none(minor):
            minor_.text = convert_to_string(minor)

        severe_ = SubElement(self, 'watchd-cfg:severe')

        if is_not_none(severe):
            severe_.text = convert_to_string(severe)

        critical_ = SubElement(self, 'watchd-cfg:critical')

        if is_not_none(critical):
            critical_.text = convert_to_string(critical)
        
        if is_not_none(operation):
            self.set('xc:operation', operation.value)
        

class WatchdogNodeThreshold(WatchdBase):
    
    @force_type
    def __init__(self, disk_threshold: DiskThreshold = None, memory_threshold: MemoryThreshold = None):
        """"watchdog node threshold."""

        super().__init__('watchd-cfg:watchdog-node-threshold')

        if is_not_none(disk_threshold):
            self.append(disk_threshold)

        if is_not_none(memory_threshold):
            self.append(memory_threshold)


class NodesBaseCfg(Cfg):
    
    @force_type
    def __init__(self, leaf_name: str):
        
        super().__init__(leaf_name)

        self.set('xmlns:config-mda-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-config-mda-cfg')


class  ActiveNode(Cfg):
    
    @force_type
    def __init__(self, node_name: str, watchdog_node_threshold: WatchdogNodeThreshold = None):
        """
        Per-node configuration for active nodes.

        node_name: str: The identifier for this node.
        """
        super().__init__('config-mda-cfg:active-node')
        
        node_name_ = SubElement(self, 'config-mda-cfg:node-name')

        if is_not_none(node_name):
            node_name_.text = node_name

        if is_not_none(watchdog_node_threshold):
            self.append(watchdog_node_threshold)


class ActiveNodesCfg(NodesBaseCfg):

    def __init__(self):
        """Per-node configuration for active nodes."""

        super().__init__('config-mda-cfg:active-nodes')

    @force_type
    def active_node(self, value: ActiveNode):
        """The configuration for an active node."""

        if is_not_none(value):
            self.append(value)


class PreconfiguredNode(Cfg):
    
    @force_type
    def __init__(self, node_name: str, watchdog_node_threshold: WatchdogNodeThreshold = None):
        """
        The configuration for a non-active node.

        node_name: str: The identifier for this node.
        """

        super().__init__('config-mda-cfg:preconfigured-node')

        node_name_ = SubElement(self, 'config-mda-cfg:node-name')

        if is_not_none(node_name):
            node_name_.text = node_name
        
        if is_not_none(watchdog_node_threshold):
            self.append(watchdog_node_threshold)

    
class PreconfiguredNodesCfg(NodesBaseCfg):

    def __init__(self):
        """preconfigured nodes."""

        super().__init__('config-mda-cfg:preconfigured-nodes')
    
    @force_type
    def preconfigured_node(self, value: PreconfiguredNode):
        """The configuration for a non-active node."""

        if is_not_none(value):
            self.append(value)
            