from datatype import TypeDef
from datadefinition import Cfg
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type
                    
                    
class RouterStaticCfg(Cfg):

    def __init__(self):
        super().__init__()
        self.set('xmlns', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ip-static-cfg')