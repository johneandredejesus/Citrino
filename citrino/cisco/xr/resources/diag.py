from datadefinition import  Oper
from xml.etree.ElementTree import SubElement
from methods import is_not_none, force_type


class Chassis(Oper):

    def __init__(self):
        """Chassis information"""
        super().__init__('sdr-invmgr-diag-oper:chassis')


class Slot(Oper):

    def __init__(self, slot_name:  str = None):
        """slot_name:  str. Slot name."""
        super().__init__('sdr-invmgr-diag-oper:slot')

        if is_not_none(slot_name):
            slot_name_ = SubElement(self, 'sdr-invmgr-diag-oper:slot-name')
            slot_name_.text = slot_name


class Slots(Oper):

    def __init__(self):
        """Table of slots"""
        super().__init__('sdr-invmgr-diag-oper:slots')
    
    def slot(self, value: Slot):

        if is_not_none(value):
            self.append(value)


class Fans(Oper):

    def __init__(self, fans_name: str = None):
        """fans_name: str. Fans name."""
        super().__init__('sdr-invmgr-diag-oper:fans')
        
        if is_not_none(fans_name):
            fans_name_ = SubElement(self, 'sdr-invmgr-diag-oper:fans-name')
            fans_name_.text = fans_name


class Fanses(Oper):

    def __init__(self):
        """Table for rack fans"""
        super().__init__('sdr-invmgr-diag-oper:fanses')

    def fans(self, value: Fans):
        
        if is_not_none(value):
            self.append(value)


class FanTray(Oper):

    def __init__(self, fan_tray_name: str = None, fanses: Fanses = None):
        """fan_tray_name: str. Fan tray name."""
        super().__init__('sdr-invmgr-diag-oper:fan-tray')
        
        if is_not_none(fan_tray_name):
            fan_tray_name_ = SubElement(self, 'sdr-invmgr-diag-oper:fan-tray-name')
            fan_tray_name_.text = fan_tray_name
        
        if is_not_none(fanses):
            self.append(fanses)


class FanTraies(Oper):

    def __init__(self):
        """"Table for rack fan trays"""
        super().__init__('sdr-invmgr-diag-oper:fan-traies')

    def fan_tray(self, value: FanTray):

        if is_not_none(value):
            self.append(value)


class PowerSupply(Oper):

    def __init__(self, power_supply_name: str = None):
        """
        power_supply_name: str. Power Supply name.
        """
        super().__init__('sdr-invmgr-diag-oper:power-supply')

        if is_not_none(power_supply_name):
            power_supply_name_ = SubElement(self, 'sdr-invmgr-diag-oper:power-supply-name')
            power_supply_name_.text = power_supply_name


class PowerSupplies(Oper):

    def __init__(self):
        """Table for rack power supply"""
        super().__init__('sdr-invmgr-diag-oper:power-supplies')

    def power_supply(self, value: PowerSupply):

        if is_not_none(value):
            self.append(value)


class PowerShelf(Oper):

    def  __init__(self, power_shelf_name: str = None, power_supplies: PowerSupplies = None):
        """power_shelf_name: str. Power shelf name."""
        super().__init__('sdr-invmgr-diag-oper:power-shelf')
        
        if is_not_none(power_shelf_name):

            power_shelf_name_ = SubElement(self, 'sdr-invmgr-diag-oper:power-shelf-name')
            power_shelf_name_.text = power_shelf_name

        if is_not_none(power_supplies):
            self.append(power_supplies)


class  PowerShelfs(Oper):
   
    def __init__(self):
        """Table for rack power shelf."""
        super().__init__('sdr-invmgr-diag-oper:power-shelfs')

    def power_shelf(self, value: PowerShelf = None):
        
        if is_not_none(value):
           self.append(value)


class  Rack(Oper):
    
    @force_type
    def __init__(self, rack_name: str = None, power_shelfs: PowerShelfs = None, 
                fan_traies: FanTraies = None, slots: Slots = None, chassis: Chassis = None):
        """rack_name: str. Rack name."""

        super().__init__('sdr-invmgr-diag-oper:rack')

        if is_not_none(rack_name):
            rack_name_ = SubElement(self, 'sdr-invmgr-diag-oper:rack-name')
            rack_name_.text = rack_name
        
        if is_not_none(power_shelfs):
            self.append(power_shelfs)
        
        if is_not_none(fan_traies):
            self.append(fan_traies)

        if is_not_none(slots):
            self.append(slots)

        if is_not_none(chassis):
            self.append(chassis)


class  Racks(Oper):
    """Table of racks"""

    def __init__(self):
        super().__init__('sdr-invmgr-diag-oper:racks')
    
    @force_type
    def rack(self, value: Rack = None):
        if is_not_none(value):
            self.append(value)
        

class DiagOper(Oper):
    
    @force_type
    def __init__(self, racks: Racks = None):
        """
        module: Cisco-IOS-XR-sdr-invmgr-diag-oper
        
        Diag information
        """
        super().__init__('sdr-invmgr-diag-oper:diag')
        self.set('xmlns:sdr-invmgr-diag-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-sdr-invmgr-diag-oper')

        if is_not_none(racks):
            self.append(racks)