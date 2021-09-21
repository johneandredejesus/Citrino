from datadefinition import Oper
from xml.etree.ElementTree import SubElement
from methods import is_not_none, force_type


class Uptime(Oper):

    def __init__(self):
        """System uptime information."""

        super().__init__('shellutil-oper:uptime')


class Clock(Oper):

    def __init__(self):
        """System clock information."""

        super().__init__('shellutil-oper:clock')


class SystemTimeOper(Oper):

    @force_type
    def __init__(self, clock: Clock = None, uptime: Uptime = None):
        """
        module: Cisco-IOS-XR-shellutil-oper.

        System time information.
        """

        super().__init__('shellutil-oper:system-time')

        self.set('xmlns:shellutil-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-oper')

        if is_not_none(clock):
            self.append(clock)

        if is_not_none(uptime):
            self.append(uptime)