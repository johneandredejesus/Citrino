from datadefinition import Act
from xml.etree.ElementTree import Element, SubElement
from methods import convert_to_string, is_not_none, force_type
from exceptions import NoneException


class TracerouteAct(Act):

    def __init__(self):
        """Cisco-IOS-XR-traceroute-act"""
        
        super().__init__('traceroute-act:traceroute')
        self.set('xmlns:traceroute-act', 'http://cisco.com/ns/yang/Cisco-IOS-XR-traceroute-act')

    @force_type
    def destination(self, destination_: str, source: str = None, timeout: int = None,
                    probe: int = None, numeric: bool = None, vrf_name: str = None, min_ttl: int = None,
                    max_ttl: int = None, port: int = None, verbose: bool = None, priority: int = None,
                    outgoing_interface: str = None):
        """
        destination_: str. Destination address or hostname.

        source: str. Source address or interface.

        timeout: int. range "0..36". Timeout in seconds.

        probe: int. range "1..64". Probe count.

        numeric: bool. Numeric display only.

        vrf_name: str. VRF name.

        min_ttl: int. range "0..255". minimum time to live.

        max_ttl: int. range "0..255". maximum time to live.

        port: int. range "0..65535". Port numbe.

        verbose: bool. verbose output.

        priority: int. range "0..15". Priority of hte packet.

        outgoing_interface: str. Outgoing interface, needed in case of traceroute to link local address.
        """

        _destination_ = SubElement(self, 'traceroute-act:destination')

        if is_not_none(destination_):
            destination_destination = SubElement(
                _destination_, 'traceroute-act:destination')
            destination_destination.text = destination_
        else:
            raise NoneException('destination_ cannot be None.')

        if is_not_none(source):
            source_ = SubElement(_destination_, 'traceroute-act:source')
            source_.text = source

        if is_not_none(timeout):
            timeout_ = SubElement(_destination_, 'traceroute-act:timeout')
            timeout_.text = convert_to_string(timeout)

        if is_not_none(probe):
            probe_ = SubElement(_destination_, 'traceroute-act:probe')
            probe_.text = convert_to_string(probe)

        if is_not_none(numeric):
            numeric_ = SubElement(_destination_, 'traceroute-act:numeric')
            numeric_.text = convert_to_string(numeric)

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(
                _destination_, 'traceroute-act:vrf-name')
            vrf_name_.text = vrf_name_

        if is_not_none(min_ttl):
            min_ttl_ = SubElement(_destination_, 'traceroute-act:min-ttl')
            min_ttl_.text = convert_to_string(min_ttl)

        if is_not_none(max_ttl):
            max_ttl_ = SubElement(_destination_, 'traceroute-act:max-ttl')
            max_ttl_.text = convert_to_string(max_ttl)

        if is_not_none(port):
            port_ = SubElement(_destination_, 'traceroute-act:port')
            port_.text = convert_to_string(port)

        if is_not_none(verbose):
            verbose_ = SubElement(_destination_, 'traceroute-act:verbose')
            verbose_.text = convert_to_string(verbose)

        if is_not_none(priority):
            priority_ = SubElement(
                _destination_, 'traceroute-act:priority')
            priority_.text = convert_to_string(priority)

        if is_not_none(outgoing_interface):
            outgoing_interface_ = SubElement(
                _destination_, 'traceroute-act:outgoing-interface')
            outgoing_interface_.text = outgoing_interface

    @force_type
    def ipv4(self, destination: str, source: str = None, timeout: int = None,
             probe: int = None, numeric: bool = None, vrf_name: str = None, min_ttl: int = None,
             max_ttl: int = None, port: int = None, verbose: bool = None):
        """
        destination: str. Destination address or hostname.

        source: str. Source address or interface.

        timeout: int. range "0..36". Timeout in seconds.

        probe: int. range "1..64". Probe count.

        numeric: bool. Numeric display only.

        vrf_name: str. VRF name.

        min_ttl: int. range "0..255". minimum time to live.

        max_ttl: int. range "0..255". maximum time to live.

        port: int. range "0..65535". Port numbe.

        verbose: bool. verbose output.
        """

        ipv4_ = SubElement(self, 'traceroute-act:ipv4')

        if is_not_none(destination):
            destination_ = SubElement(ipv4_, 'traceroute-act:destination')
            destination_.text = destination
        else:
            raise NoneException('destination cannot be None.')

        if is_not_none(source):
            source_ = SubElement(ipv4_, 'traceroute-act:source')
            source_.text = source

        if is_not_none(timeout):
            timeout_ = SubElement(ipv4_, 'traceroute-act:timeout')
            timeout_.text = convert_to_string(timeout)

        if is_not_none(probe):
            probe_ = SubElement(ipv4_, 'traceroute-act:probe')
            probe_.text = convert_to_string(probe)

        if is_not_none(numeric):
            numeric_ = SubElement(ipv4_, 'traceroute-act:numeric')
            numeric_.text = convert_to_string(numeric)

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(ipv4_, 'traceroute-act:vrf-name')
            vrf_name_.text = vrf_name_

        if is_not_none(min_ttl):
            min_ttl_ = SubElement(ipv4_, 'traceroute-act:min-ttl')
            min_ttl_.text = convert_to_string(min_ttl)

        if is_not_none(max_ttl):
            max_ttl_ = SubElement(ipv4_, 'traceroute-act:max-ttl')
            max_ttl_.text = convert_to_string(max_ttl)

        if is_not_none(port):
            port_ = SubElement(ipv4_, 'traceroute-act:port')
            port_.text = convert_to_string(port)

        if is_not_none(verbose):
            verbose_ = SubElement(ipv4_, 'traceroute-act:verbose')
            verbose_.text = convert_to_string(verbose)

    @force_type
    def ipv6(self, destination: str, source: str = None, timeout: int = None,
             probe: int = None, numeric: bool = None, vrf_name: str = None, min_ttl: int = None,
             max_ttl: int = None, port: int = None, verbose: bool = None, priority: int = None,
             outgoing_interface: str = None):
        """
        destination: str. Destination address or hostname.

        source: str. Source address or interface.

        timeout: int. range "0..36". Timeout in seconds.

        probe: int. range "1..64". Probe count.

        numeric: bool. Numeric display only.

        vrf_name: str. VRF name.

        min_ttl: int. range "0..255". minimum time to live.

        max_ttl: int. range "0..255". maximum time to live.

        port: int. range "0..65535". Port numbe.

        verbose: bool. verbose output.

        priority: int. range "0..15". Priority of hte packet.

        outgoing_interface: str. Outgoing interface, needed in case of traceroute to link local address.
        """

        ipv6_ = SubElement(self, 'traceroute-act:ipv6')

        if is_not_none(destination):
            destination_ = SubElement(ipv6_, 'traceroute-act:destination')
            destination_.text = destination
        else:
            raise NoneException('destination cannot be None')

        if is_not_none(source):
            source_ = SubElement(ipv6_, 'traceroute-act:source')
            source_.text = source

        if is_not_none(timeout):
            timeout_ = SubElement(ipv6_, 'traceroute-act:timeout')
            timeout_.text = convert_to_string(timeout)

        if is_not_none(probe):
            probe_ = SubElement(ipv6_, 'traceroute-act:probe')
            probe_.text = convert_to_string(probe)

        if is_not_none(numeric):
            numeric_ = SubElement(ipv6_, 'traceroute-act:numeric')
            numeric_.text = convert_to_string(numeric)

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(ipv6_, 'traceroute-act:vrf-name')
            vrf_name_.text = vrf_name_

        if is_not_none(min_ttl):
            min_ttl_ = SubElement(ipv6_, 'traceroute-act:min-ttl')
            min_ttl_.text = convert_to_string(min_ttl)

        if is_not_none(max_ttl):
            max_ttl_ = SubElement(ipv6_, 'traceroute-act:max-ttl')
            max_ttl_.text = convert_to_string(max_ttl)

        if is_not_none(port):
            port_ = SubElement(ipv6_, 'traceroute-act:port')
            port_.text = convert_to_string(port)

        if is_not_none(verbose):
            verbose_ = SubElement(ipv6_, 'traceroute-act:verbose')
            verbose_.text = convert_to_string(verbose)

        if is_not_none(priority):
            priority_ = SubElement(ipv6_, 'traceroute-act:priority')
            priority_.text = convert_to_string(priority)

        if is_not_none(outgoing_interface):
            outgoing_interface_ = SubElement(ipv6_, 'traceroute-act:outgoing-interface')
            outgoing_interface_.text = outgoing_interface