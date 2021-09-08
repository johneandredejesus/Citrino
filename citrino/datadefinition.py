from methods import is_not_none, force_type
from exceptions import InvalidOperationException, NotConnectedException
from datatype import TypeDef
from xml.etree.ElementTree import Element
from abc import ABC, abstractmethod
from methods import is_operation
from typing import Any


class OperationEnum():

    class Operation(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    DELETE = Operation('delete')
    MERGE = Operation('merge')
    REPLACE = Operation('replace')
    CREATE = Operation('create')
    REMOVE = Operation('remove')


class Manipulator(Element):

    def __init__(self, tag: str, *args: Any, **kwargs: Any):
        super().__init__(tag, *args, **kwargs)


class Cfg(Manipulator):

    def __init__(self, tag: str, *args: Any, **kwargs: Any):
        super().__init__(tag, *args, **kwargs)


class Oper(Manipulator):

    def __init__(self, tag: str, *args: Any, **kwargs: Any):
        super().__init__(tag, *args, **kwargs)


class Act(Manipulator):

    def __init__(self, tag: str, *args: Any, **kwargs: Any):
        super().__init__(tag, *args, **kwargs)


class OpenConfig(Manipulator):

    def __init__(self, tag: str, *args: Any, **kwargs: Any):
        super().__init__(tag, *args, **kwargs)
