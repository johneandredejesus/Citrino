from datatype import TypeDef
from datadefinition import(OperationEnum,
                           Cfg,
                           Oper,
                           Act,
                           OpenConfig)
from xml.etree.ElementTree import(tostring, Element, SubElement)
from methods import convert_to_string, is_not_none, force_type


class LocalRoutingOpenConfig(OpenConfig):

    def __init__(self):
        super().__init__()
