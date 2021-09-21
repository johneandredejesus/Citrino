from datadefinition import Act
from xml.etree.ElementTree import Element, SubElement
from methods import convert_to_string, is_not_none, force_type
from exceptions import NoneException


class PingAct(Act):

    def __init__(self):
        """module: Cisco-IOS-XR-ping-act"""
        
        super().__init__('ping-act:ping')
        self.set('xmlns:ping-act', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ping-act')

    @force_type
    def destination(self, destination_: str, repeat_count: int = None,
                    data_size: int = None, timeout: int = None, interval: int = None,
                    pattern: int = None, sweep: bool = None, vrf_name: str = None,
                    source: str = None, verbose: bool = None, type_of_service: int = None,
                    do_not_frag: bool = None, validate: bool = None, priority: int = None,
                    outgoing_interface: str = None):
        """
        destination_: str. Ping destination address or hostname.

        repeat_count: int. range "1..64". Number of ping packets to be sent out.

        data_size: int. range "36..18024". Size of ping packet.

        timeout: int. range "0..36". Timeout in seconds.

        interval: int. range "0..3600". Ping interval in milli seconds.

        pattern: int. Pattern of payload data.

        sweep: bool. Sweep is enabled.

        vrf_name: str. VRF name.

        source: str. Source address or interface.

        verbose: bool. Validate return packet.

        type_of_service: int. range "0..255. Type of Service.

        do_not_frag: bool. Do Not Fragment.

        validate: bool. Validate return packet.

        priority: int. range "0..15". Priority of the packet.

        outgoing_interface: str. Outgoing interface, needed in case of ping to link local address.
        """

        _destination_ = SubElement(self, 'ping-act:destination')

        if is_not_none(destination_):
            destination_destination = SubElement(
                _destination_, 'ping-act:destination')
            destination_destination.text = destination_
        else:
            raise NoneException('destination_ cannot be None.')

        if is_not_none(repeat_count):
            repeat_count_ = SubElement(_destination_, 'ping-act:repeat-count')
            repeat_count_.text = convert_to_string(repeat_count)

        if is_not_none(data_size):
            data_size_ = SubElement(_destination_, 'ping-act:data-size')
            data_size_.text = convert_to_string(data_size)

        if is_not_none(timeout):
            timeout_ = SubElement(_destination_, 'ping-act:timeout')
            timeout_.text = convert_to_string(timeout)

        if is_not_none(interval):
            interval_ = SubElement(_destination_, 'ping-act:interval')
            interval_.text = convert_to_string(interval)

        if is_not_none(pattern):
            pattern_ = SubElement(_destination_, 'ping-act:pattern')
            pattern_.text = convert_to_string(pattern)

        if is_not_none(sweep):
            sweep_ = SubElement(_destination_, 'ping-act:sweep')
            sweep_.text = convert_to_string(sweep)

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(_destination_, 'ping-act:vrf-name')
            vrf_name_.text = vrf_name

        if is_not_none(source):
            source_ = SubElement(_destination_, 'ping-act:source')
            source_.text = source

        if is_not_none(verbose):
            verbose_ = SubElement(_destination_, 'ping-act:verbose')
            verbose_.text = convert_to_string(verbose)

        if is_not_none(type_of_service):
            type_of_service_ = SubElement(
                _destination_, 'ping-act:type-of-service')
            type_of_service_.text = convert_to_string(type_of_service)

        if is_not_none(do_not_frag):
            do_not_frag_ = SubElement(_destination_, 'ping-act:do-not-frag')
            do_not_frag_.text = convert_to_string(do_not_frag)

        if is_not_none(validate):
            validate_ = SubElement(_destination_, 'ping-act:validate')
            validate_.text = convert_to_string(validate)

        if is_not_none(priority):
            priority_ = SubElement(_destination_, 'ping-act:priority')
            priority_.text = convert_to_string(priority)

        if is_not_none(outgoing_interface):
            outgoing_interface_ = SubElement(
                _destination_, 'ping-act:outgoing-interface')
            outgoing_interface_.text = outgoing_interface

    @force_type
    def ipv4(self, destination: str, repeat_count: int = None,
             data_size: int = None, timeout: int = None, interval: int = None,
             pattern: int = None, sweep: bool = None, vrf_name: str = None,
             source: str = None, verbose: bool = None, type_of_service: int = None,
             do_not_frag: bool = None, validate: bool = None,):
        """
        destination: str. Ping destination address or hostname.

        repeat_count: int. range "1..64". Number of ping packets to be sent out.

        data_size: int. range "36..18024". Size of ping packet.

        timeout: int. range "0..36". Timeout in seconds.

        interval: int. range "0..3600". Ping interval in milli seconds.

        pattern: int. Pattern of payload data.

        sweep: bool. Sweep is enabled.

        vrf_name: str. VRF name.

        source: str. Source address or interface.

        verbose: bool. Validate return packet.

        type_of_service: int. range "0..255. Type of Service.

        do_not_frag: bool. Do Not Fragment.

        validate: bool. Validate return packet.
        """
        ipv4_ = SubElement(self, 'ping-act:ipv4')

        if is_not_none(destination):
            destination_ = SubElement(ipv4_, 'ping-act:destination')
            destination_.text = destination
        else:
            raise NoneException('destination cannot be None.')

        if is_not_none(repeat_count):
            repeat_count_ = SubElement(ipv4_, 'ping-act:repeat-count')
            repeat_count_.text = convert_to_string(repeat_count)

        if is_not_none(data_size):
            data_size_ = SubElement(ipv4_, 'ping-act:data-size')
            data_size_.text = convert_to_string(data_size)

        if is_not_none(timeout):
            timeout_ = SubElement(ipv4_, 'ping-act:timeout')
            timeout_.text = convert_to_string(timeout)

        if is_not_none(interval):
            interval_ = SubElement(ipv4_, 'ping-act:interval')
            interval_.text = convert_to_string(interval)

        if is_not_none(pattern):
            pattern_ = SubElement(ipv4_, 'ping-act:pattern')
            pattern_.text = convert_to_string(pattern)

        if is_not_none(sweep):
            sweep_ = SubElement(ipv4_, 'ping-act:sweep')
            sweep_.text = convert_to_string(sweep)

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(ipv4_, 'ping-act:vrf-name')
            vrf_name_.text = vrf_name

        if is_not_none(source):
            source_ = SubElement(ipv4_, 'ping-act:source')
            source_.text = source

        if is_not_none(verbose):
            verbose_ = SubElement(ipv4_, 'ping-act:verbose')
            verbose_.text = convert_to_string(verbose)

        if is_not_none(type_of_service):
            type_of_service_ = SubElement(ipv4_, 'ping-act:type-of-service')
            type_of_service_.text = convert_to_string(type_of_service)

        if is_not_none(do_not_frag):
            do_not_frag_ = SubElement(ipv4_, 'ping-act:do-not-frag')
            do_not_frag_.text = convert_to_string(do_not_frag)

        if is_not_none(validate):
            validate_ = SubElement(ipv4_, 'ping-act:validate')
            validate_.text = convert_to_string(validate)

    @force_type
    def ipv6(self, destination: str, repeat_count: int = None,
             data_size: int = None, timeout: int = None, interval: int = None,
             pattern: int = None, sweep: bool = None, vrf_name: str = None,
             source: str = None, verbose: bool = None, priority: int = None,
             outgoing_interface: str = None):
        """
        destination: str. Ping destination address or hostname.

        repeat_count: int. range "1..64". Number of ping packets to be sent out.

        data_size: int. range "36..18024". Size of ping packet.

        timeout: int. range "0..36". Timeout in seconds.

        interval: int. range "0..3600". Ping interval in milli seconds.

        pattern: int. Pattern of payload data.

        sweep: bool. Sweep is enabled.

        vrf_name: str. VRF name.

        source: str. Source address or interface.

        verbose: bool. Validate return packet.

        priority: int. range "0..15". Priority of the packet.

        outgoing_interface: str. Outgoing interface, needed in case of ping to link local address.

        """
        ipv6_ = SubElement(self, 'ping-act:ipv6')

        if is_not_none(destination):
            destination_ = SubElement(ipv6_, 'ping-act:destination')
            destination_.text = destination
        else:
            raise NoneException('destination cannot be None.')

        if is_not_none(repeat_count):
            repeat_count_ = SubElement(ipv6_, 'ping-act:repeat-count')
            repeat_count_.text = convert_to_string(repeat_count)

        if is_not_none(data_size):
            data_size_ = SubElement(ipv6_, 'ping-act:data-size')
            data_size_.text = convert_to_string(data_size)

        if is_not_none(timeout):
            timeout_ = SubElement(ipv6_, 'ping-act:timeout')
            timeout_.text = convert_to_string(timeout)

        if is_not_none(interval):
            interval_ = SubElement(ipv6_, 'ping-act:interval')
            interval_.text = convert_to_string(interval)

        if is_not_none(pattern):
            pattern_ = SubElement(ipv6_, 'ping-act:pattern')
            pattern_.text = convert_to_string(pattern)

        if is_not_none(sweep):
            sweep_ = SubElement(ipv6_, 'ping-act:sweep')
            sweep_.text = convert_to_string(sweep)

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(ipv6_, 'ping-act:vrf-name')
            vrf_name_.text = vrf_name

        if is_not_none(source):
            source_ = SubElement(ipv6_, 'ping-act:source')
            source_.text = source

        if is_not_none(verbose):
            verbose_ = SubElement(ipv6_, 'ping-act:verbose')
            verbose_.text = convert_to_string(verbose)

        if is_not_none(priority):
            priority_ = SubElement(ipv6_, 'ping-act:priority')
            priority_.text = convert_to_string(priority)

        if is_not_none(outgoing_interface):
            outgoing_interface_ = SubElement(
                ipv6_, 'ping-act:outgoing-interface')
            outgoing_interface_.text = outgoing_interface
