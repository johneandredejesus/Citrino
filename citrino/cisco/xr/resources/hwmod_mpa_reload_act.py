from datadefinition import Act
from xml.etree.ElementTree import SubElement
from methods import is_not_none, force_type


class  HwmodMPAReload(Act):
    
    def __init__(self):
        """
        module: Cisco-IOS-XR-hwmod-mpa-reload-act.

        Execute subslot h/w module operations.
        """

        super().__init__('hwmod-mpa-reload-act:hw-module-subslot')

        self.set('xmlns:hwmod-mpa-reload-act', 'http://cisco.com/ns/yang/Cisco-IOS-XR-hwmod-mpa-reload-act')
    
    @force_type
    def subslot(self, value: str = None):
        """Fully qualified location specification."""

        subslot_ = SubElement(self, 'hwmod-mpa-reload-act:subslot')
        
        if is_not_none(value):
            subslot_.text = value

    def reload(self):
        """Cycle subslot h/w reset."""

        SubElement(self, 'hwmod-mpa-reload-act:reload')