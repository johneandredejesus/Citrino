from datadefinition import OperationEnum, Cfg
from xml.etree.ElementTree import SubElement
from methods import is_not_none, force_type


class HostNamesCfg(Cfg):
    
    @force_type
    def __init__(self, host_name: str = None, operation: OperationEnum.Operation = None):
        """
        module: Cisco-IOS-XR-shellutil-cfg.

        Container Schema for hostname configuration.

        host_name: str. Configure system's hostname.
        """

        super().__init__('shellutil-cfg:host-names')

        self.set('xmlns:shellutil-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-cfg')

        host_name_ = SubElement(self, 'shellutil-cfg:host-name')

        if is_not_none(host_name):
            host_name_.text = host_name
        
        if is_not_none(operation):
            host_name_.set('xc:operation', operation.value)

            