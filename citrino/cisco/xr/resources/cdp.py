from datatype import TypeDef
from datadefinition import(OperationEnum,
                           Cfg,
                           Oper,
                           OpenConfig)
from xml.etree.ElementTree import(tostring, Element, SubElement)
from methods import convert_to_string, is_not_none, force_type


class CDPOper(Oper):

    """module: Cisco-IOS-XR-cdp-oper"""

    def __init__(self):
        super().__init__()
        self.set('xmlns:cdp-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-cdp-oper')
