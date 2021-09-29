from datadefinition import Oper
from xml.etree.ElementTree import SubElement
from methods import is_not_none, force_type


class CPUUtilization(Oper):
    
    @force_type
    def __init__(self, node_name: str):
        """
        Processes CPU utilization information.

        node_name: str. Node name.
        """
        super().__init__('wdsysmon-fd-oper:cpu-utilization')

        if is_not_none(node_name):
            node_name_ = SubElement(self, 'wdsysmon-fd-oper:node-name')
            node_name_.text = node_name


class SystemMonitoringOper(Oper):

    def __init__(self):
        """
        module: Cisco-IOS-XR-wdsysmon-fd-oper.
        
        Processes operational data.
        """
        super().__init__('wdsysmon-fd-oper:system-monitoring')

        self.set('xmlns:wdsysmon-fd-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-wdsysmon-fd-oper')
    
    @force_type
    def cpu_utilization(self, value: CPUUtilization):
        """Processes CPU utilization information."""
        
        if is_not_none(value):
            self.append(value)