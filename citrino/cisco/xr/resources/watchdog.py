from datadefinition import OperationEnum, Cfg, Oper
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type


class  ThresholdMemoryCfg(Cfg):
    
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
        


class  DiskLimitCfg(Cfg):
    
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
               

class WatchdBaseCfg(Cfg):
    
    @force_type
    def __init__(self, module_name: str):

        """module: Cisco-IOS-XR-watchd-cfg."""

        super().__init__(module_name)

        self.set('xmlns:watchd-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-watchd-cfg')


class WatchdogCfg(WatchdBaseCfg):
    
    @force_type
    def __init__(self, threshold_memory: ThresholdMemoryCfg = None, disk_limit: DiskLimitCfg = None):
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


class WatchdCfg(WatchdBaseCfg):

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


class DiskThresholdCfg(Cfg):
    
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
           

class MemoryThresholdCfg(Cfg):
    
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
        

class WatchdogNodeThresholdCfg(WatchdBaseCfg):
    
    @force_type
    def __init__(self, disk_threshold: DiskThresholdCfg = None, memory_threshold: MemoryThresholdCfg = None):
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


class  ActiveNodeCfg(Cfg):
    
    @force_type
    def __init__(self, node_name: str, watchdog_node_threshold: WatchdogNodeThresholdCfg = None):
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
    def active_node(self, value: ActiveNodeCfg):
        """The configuration for an active node."""

        if is_not_none(value):
            self.append(value)


class PreconfiguredNodeCfg(Cfg):
    
    @force_type
    def __init__(self, node_name: str, watchdog_node_threshold: WatchdogNodeThresholdCfg = None):
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
    def preconfigured_node(self, value: PreconfiguredNodeCfg):
        """The configuration for a non-active node."""

        if is_not_none(value):
            self.append(value)

class CurrentThrottleOper(Oper):

    def __init__(self):
        """Current throttle details."""

        super().__init__('wd-oper:current-throttle')

class OverloadStateOper(Oper):
    
    @force_type
    def __init__(self, current_throttle: CurrentThrottleOper = None):
        """Display overload control state."""

        super().__init__('wd-oper:overload-state')

        if is_not_none(current_throttle):
            self.append(current_throttle)

class MemoryStateOper(Oper):

    def __init__(self):
        """Memory state."""

        super().__init__('wd-oper:memory-state')

class ConfiguredOper(Oper):

    def __init__(self):
        """Memory configured by user."""

        super().__init__('wd-oper:configured')

class MemoryOper(Oper):

    def __init__(self):
        """Memory information."""

        super().__init__('wd-oper:memory')

class ConfiguredMemoryOper(Oper):

    def __init__(self):
        """Configured memory."""

        super().__init__('wd-oper:configured-memory')

class DefaultOper(Oper):
    
    @force_type
    def __init__(self, configured_memory: ConfiguredMemoryOper = None, memory: MemoryOper = None):
        """System default memory."""

        super().__init__('wd-oper:default')

        if is_not_none(configured_memory):
            self.append(configured_memory)
        
        if is_not_none(memory):
            self.append(memory)
        
class ThresholdMemoryOper(Oper):
    
    @force_type
    def __init__(self, default: DefaultOper = None, configured: ConfiguredOper = None):
        """Threshold memory."""

        super().__init__('wd-oper:threshold-memory')

        if is_not_none(default):
            self.append(default)
        
        if is_not_none(configured):
            self.append(configured)

class NodeOper(Oper):
    
    @force_type
    def __init__(self, node_name: str, threshold_memory: ThresholdMemoryOper = None, 
                       memory_state: MemoryStateOper= None, overload_state: OverloadStateOper = None):
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
        
class NodesOper(Oper):

    def __init__(self):
        """List of nodes."""

        super().__init__('wd-oper:nodes')
    
    @force_type
    def node(self, value: NodeOper):
        
        if is_not_none(value):
            self.append(value)

class WatchdogOper(Oper):
    
    @force_type
    def __init__(self, nodes: NodesOper = None):
        """"
        module: Cisco-IOS-XR-wd-oper
        
        Watchdog information.
        """
        
        super().__init__('wd-oper:watchdog')

        self.set('xmlns:wd-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-wd-oper')

        if is_not_none(nodes):
            self.append(nodes)