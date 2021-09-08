from datatype import TypeDef
from datadefinition import OperationEnum, Cfg, OpenConfig
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type
from exceptions import NoneException


class IPV4ReachableEnum():

    """
    ANY: Source is reachable via any interface.

    RECEIVED: Source is reachable via interface on which packet was received.
    """

    class IPV4Reachable(TypeDef):

        """Ipv4 reachable"""

        def __init__(self, value):
            super().__init__(value)

    ANY = IPV4Reachable('any')
    RECEIVED = IPV4Reachable('received')


class IPV4SelfPingEnum():

    """
    DISABLED: Doesn't allow router to ping itself.

    ENABLED: Allow router to ping itself.
    """

    class IPV4SelfPing(TypeDef):

        """Ipv4 self ping"""

        def __init__(self, value):
            super().__init__(value)

    DISABLED = IPV4SelfPing('disabled')
    ENABLED = IPV4SelfPing('enabled')


class IPV4DefaultPingEnum():

    """
    DISABLED: Default route is not allowed to match when checking source address.

    ENABLED: Allow default route to match when checking source address
    """

    class IPV4DefaultPing(TypeDef):

        """Ipv4 default ping"""

        def __init__(self, value):
            super().__init__(value)

    DISABLED = IPV4DefaultPing('disabled')
    ENABLED = IPV4DefaultPing('enabled')


class DhcpClientOptionCodeEnum():

    """Dhcp client option code"""

    class DhcpClientOptionCode(TypeDef):

        """"Vendor id  DHCP Discover"""

        def __init__(self, value):
            super().__init__(value)

    CODE_60 = DhcpClientOptionCode('60')


class IPV4InterfaceQPPBEnum():

    """
    Ipv4 interface qppb.

    IP_PRECEDENCE: Enable IP precedence based QPPB.

    QOS_GROUP: Enable QoS-group based QPPB.

    BOTH: Enable both IP precedence and QoS-group based QPPB.
    """

    class Ipv4InterfaceQPPB(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    IP_PRECEDENCE = Ipv4InterfaceQPPB('ip-precedence')
    QOS_GROUP = Ipv4InterfaceQPPB('qos-group')
    BOTH = Ipv4InterfaceQPPB('both')


class BGPPAInput(Cfg):

    @force_type
    def __init__(self, source_accounting: bool = None, destination_accounting: bool = None, operation: OperationEnum.Operation = None):
        """
        Interface ipv4 bgp configuration.

        BGP PA configuration on source.

        source_accounting: boolean.

        destination_accounting: boolean.
        """

        super().__init__('ipv4-io-cfg:input')

        if is_not_none(source_accounting):
            source_accounting_ = SubElement(self, 'ipv4-io-cfg:source-accounting')
            source_accounting_.text = convert_to_string(source_accounting)

        if is_not_none(destination_accounting):
            destination_accounting_ = SubElement(self, 'ipv4-io-cfg:destination-accounting')
            destination_accounting_.text = convert_to_string(destination_accounting)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)


class BGPPAOutput(Cfg):
    
    @force_type
    def __init__(self, source_accounting: bool = None, destination_accounting: bool = None, operation: OperationEnum.Operation = None):
        """
        Interface ipv4 bgp configuration.

        BGP PA configuration on source.

        source_accounting: boolean.

        destination_accounting: boolean.
        """

        super().__init__('ipv4-io-cfg:output')

        if is_not_none(source_accounting):
            source_accounting_ = SubElement(self, 'ipv4-io-cfg:source-accounting')
            source_accounting_.text = convert_to_string(source_accounting)

        if is_not_none(destination_accounting):
            destination_accounting_ = SubElement(self, 'ipv4-io-cfg:destination-accounting')
            destination_accounting_.text = convert_to_string(destination_accounting)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)


class BGPQPPB(Cfg):
    
    @force_type
    def __init__(self, source: IPV4InterfaceQPPBEnum.Ipv4InterfaceQPPB = None, destination: IPV4InterfaceQPPBEnum.Ipv4InterfaceQPPB = None,
                 operation: OperationEnum.Operation = None):
        """
        Interface ipv4 bgp policy propagation configuration.

        source: Ipv4InterfaceQPPB. QPPB configuration on source.

        destination: Ipv4InterfaceQPPB. QPPB configuration on destination.
        """

        super().__init__('ipv4-io-cfg:qppb')

        input = SubElement(self, 'ipv4-io-cfg:input')

        if is_not_none(source):
            source_ = SubElement(input, 'ipv4-io-cfg:source')
            source_.text = source.value

        if is_not_none(destination):
            destination_ = SubElement(input, 'ipv4-io-cfg:destination')
            destination_.text = destination.value

        if is_not_none(operation):
            input.set('xc:operation', operation.value)


class BGPFlowTag(Cfg):
   
    @force_type
    def __init__(self, source: bool = None, destination: bool = None, operation: OperationEnum.Operation = None):
        """
        Interface ipv4 bgp policy propagation flow tag configuration.

        source: boolean. FlowTag configuration on source.

        destination: boolean. FlowTag configuration on destination.
        """
        super().__init__('ipv4-io-cfg:flow-tag')

        flow_tag_input = SubElement(self, 'ipv4-io-cfg:flow-tag-input')

        if is_not_none(source):
            source_ = SubElement(flow_tag_input, 'ipv4-io-cfg:source')
            source_.text = convert_to_string(source)

        if is_not_none(destination):
            destination_ = SubElement(flow_tag_input, 'ipv4-io-cfg:destination')
            destination_.text = convert_to_string(destination)

        if is_not_none(operation):
            flow_tag_input.set('xc:operation', operation.value)


class SecondariesAddress(Cfg):

    def __init__(self):
        """
        Specify a secondary address.
        """

        super().__init__('ipv4-io-cfg:secondaries')

    def secondary(self, address: str = None, netmask: str = None, route_tag: int = None, operation: OperationEnum.Operation = None):
        """
        address: inet:ipv4-address-no-zone: str. Secondary IP address.

        netmask: inet:ipv4-address-no-zone: str. Netmask.

        route_tag: int. RouteTag. Range "1..4294967295.
       """

        secondary_ = SubElement(self, 'ipv4-io-cfg:secondary')

        if is_not_none(address):
            address_ = SubElement(secondary_, 'ipv4-io-cfg:address')
            address_.text = address

        if is_not_none(netmask):
            netmask_ = SubElement(secondary_, 'ipv4-io-cfg:netmask')
            netmask_.text = netmask

        if is_not_none(route_tag):
            route_tag_ = SubElement(secondary_, 'ipv4-io-cfg:route-tag')
            route_tag_.text = convert_to_string(route_tag)

        if is_not_none(operation):
            secondary_.set('xc:operation', operation.value)


class PrimaryAddress(Cfg):
    
    @force_type
    def __init__(self, address: str = None, netmask: str = None, route_tag: int = None, operation: OperationEnum.Operation = None):
        """
        Indicates a primary node is configured.

        address: inet:ipv4-address-no-zone: str. IP address.

        netmask: inet:ipv4-address-no-zone: str. Netmask.

        route_tag: int. RouteTag. Range "1..4294967295.
        """

        super().__init__('ipv4-io-cfg:primary')

        if is_not_none(address):
            address_ = SubElement(self, 'ipv4-io-cfg:address')
            address_.text = address

        if is_not_none(netmask):
            netmask_ = SubElement(self, 'ipv4-io-cfg:netmask')
            netmask_.text = netmask

        if is_not_none(route_tag):
            route_tag_ = SubElement(self, 'ipv4-io-cfg:route-tag')
            route_tag_.text = convert_to_string(route_tag)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)


class DHCPAddress(Cfg):
    
    @force_type
    def __init__(self, operation: OperationEnum.Operation = None):
        """
        IPv4 address and Mask negotiated via DHCP. Enable DHCP client on an interface.
        """

        super().__init__('ipv4-io-cfg:dhcp')

        if is_not_none(operation):
            self.set('xc:operation', operation.value)

    def enabled(self):
        """
        enabled:  Enable DHCP client on an interface.
        """

        SubElement(self, 'ipv4-io-cfg:enabled')

    @force_type
    def option_code(self, option_code_: DhcpClientOptionCodeEnum.DhcpClientOptionCode = None):
        """
        option_code: DhcpClientOptionCodeEnum. DHCP option code.
        """
        if is_not_none(option_code_):
            _option_code_ = SubElement(self, 'ipv4-io-cfg:option-code')
            _option_code_.text = option_code_.value

    @force_type
    def pattern(self, pattern_: str):
        """
        pattern: str. Vendor id str.
        """

        if is_not_none(pattern_):
            _pattern_ = SubElement(self, 'ipv4-io-cfg:pattern')
            _pattern_.text = pattern_

    @force_type
    def _format(self, format_: int):
        """ 
        format_: int. Format type.
        """
        if is_not_none(self, format_):
            _format_ = SubElement(self, 'ipv4-io-cfg:format')
            _format_.text = convert_to_string(format_)


class HelperAddresses(Cfg):

    def __init__(self):
        super().__init__('ipv4-io-cfg:helper-addresses')

    def helper_address(self, vrf_name: str, address: str,  operation: OperationEnum.Operation = None):
        """
        The set of IP destination addresses for UDP broadcasts.

        vrf_name: str. VRF name. Length "1..32".

        address: str. IP destination address.  An IP destination addresses for UDP broadcasts.
        """

        helper_address_ = SubElement(self, 'ipv4-io-cfg:helper-address')

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(helper_address_, 'ipv4-io-cfg:vrf-name')
            vrf_name_.text = vrf_name
        else:
            raise NoneException('vrf_name cannot be None.')

        if is_not_none(address):
            address_ = SubElement(helper_address_, 'ipv4-io-cfg:address')
            address_.text = address
        else:
            raise NoneException('address cannot be None.')

        if is_not_none(operation):
            helper_address_.set('xc:operation', operation.value)


class IPV4NetworkCfg(Cfg):

    def __init__(self):
        """module Cisco-IOS-XR-ipv4-io-cfg"""

        super().__init__('ipv4-io-cfg:ipv4-network')

        self.set('xmlns:ipv4-io-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg')

    @force_type
    def bgp(self, qppb: BGPQPPB = None, bgp_flow_tag: BGPFlowTag = None):
        """
        qppb: BGPQPPB. Interface ipv4 bgp policy propagation configuration.

        bgp_flow_tag: BGPFlowTag. Interface ipv4 bgp policy propagation flow tag configuration.

        """
        bgp_ = SubElement(self, 'ipv4-io-cfg:bgp')

        if is_not_none(qppb):
            bgp_.append(qppb)

        if is_not_none(bgp_flow_tag):
            bgp_.append(bgp_flow_tag)

    @force_type
    def bgp_pa(self, bgp_pa_input: BGPPAInput = None, bgp_pa_output: BGPPAOutput = None):
        """
        bgp_pa_input: BGPPAInput. Interface ipv4 bgp configuration.

        bgp_pa_output: BGPPAOutput. Interface ipv4 bgp configuration.
        """

        bgp_pa_ = SubElement(self, 'ipv4-io-cfg:bgp-pa')

        if is_not_none(bgp_pa_input):
            bgp_pa_.append(bgp_pa_input)

        if is_not_none(bgp_pa_output):
            bgp_pa_.append(bgp_pa_output)

    @force_type
    def verify(self, reachable: IPV4ReachableEnum.IPV4Reachable = None, self_ping: IPV4SelfPingEnum.IPV4SelfPing = None,
               default_ping: IPV4DefaultPingEnum.IPV4DefaultPing = None, operation: OperationEnum.Operation = None):
        """
        Enable Verify handling for this interface.

        reachable: IPV4Reachable. Source is reachable via any interface or interface on which packet was received.

        self_ping: IPV4SelfPing. Allow router to ping itself (opens vulnerability in verification).

        default_ping: IPV4DefaultPing. Allow default route to match when checking source address.
        """

        verify = SubElement(self, 'ipv4-io-cfg:verify')

        if is_not_none(reachable):
            reachable_ = SubElement(verify, 'ipv4-io-cfg:reachable')
            reachable_.text = reachable.value

        if is_not_none(self_ping):
            self_ping_ = SubElement(verify, 'ipv4-io-cfg:self-ping')
            self_ping_.text = self_ping.value

        if is_not_none(default_ping):
            default_ping_ = SubElement(verify, 'ipv4-io-cfg:default-ping')
            default_ping_.text = default_ping.value

        if is_not_none(operation):
            verify.set('xc:operation', operation.value)

    @force_type
    def addresses(self, secondaries_address: SecondariesAddress = None, primary_address: PrimaryAddress = None,
                  dhcp_address: DHCPAddress = None, unnumbered: str = None, operation: OperationEnum.Operation = None):
        """
        secondaries_address: SecondariesAddress. Specify a secondary address.

        primary_address: PrimaryAddress. Indicates a primary node is configured.

        dhcp_address: DHCPAddress. IPv4 address and Mask negotiated via DHCP. Enable DHCP client on an interface.

        unnumbered: str. Enable IP processing without an explicit address.
        """

        addresses_ = SubElement(self, 'ipv4-io-cfg:addresses')

        if is_not_none(secondaries_address):
            addresses_.append(secondaries_address)

        if is_not_none(primary_address):
            addresses_.append(primary_address)

        if is_not_none(dhcp_address):
            addresses_.append(dhcp_address)

        if is_not_none(unnumbered):
            unnumbered_ = SubElement(addresses_, 'ipv4-io-cfg:unnumbered')
            unnumbered_.text = unnumbered

        if is_not_none(operation):
            addresses_.set('xc:operation', operation.value)

    @force_type
    def helper_addresses(self, helper_addresses_: HelperAddresses):
        """
        The set of IP destination addresses for UDP broadcasts.
        """

        if is_not_none(helper_addresses_):
            self.append(helper_addresses_)

    @force_type
    def forwarding_enable(self, operation: OperationEnum.Operation = None):
        """
        IPv4 forwarding to get enabled on an interface.
        """

        forwarding_enable_ = SubElement(self, 'ipv4-io-cfg:forwarding-enable')

        if is_not_none(operation):
            forwarding_enable_.set('xc:operation', operation.value)

    @force_type
    def icmp_mask_reply(self, operation: OperationEnum.Operation = None):
        """
        The flag for enabling sending of ICMP mask reply messages.
        """

        icmp_mask_reply_ = SubElement(self, 'ipv4-io-cfg:icmp-mask-reply')

        if is_not_none(operation):
            icmp_mask_reply_.set('xc:operation', operation.value)

    @force_type
    def tcp_mss_adjust_enable(self, operation: OperationEnum.Operation = None):
        """
        Enable TCP MSS Adjust on an interface.
        """

        tcp_mss_adjust_enable_ = SubElement(self, 'ipv4-io-cfg:tcp-mss-adjust-enable')

        if is_not_none(operation):
            tcp_mss_adjust_enable_.set('xc:operation', operation.value)

    @force_type
    def ttl_propagate_disable(self, operation: OperationEnum.Operation = None):
        """
        Disable TTL propagate on an interface.
        """

        ttl_propagate_disable_ = SubElement(self, 'ipv4-io-cfg:ttl-propagate-disable')

        if is_not_none(operation):
            ttl_propagate_disable_.set('xc:operation', operation.value)

    @force_type
    def point_to_point(self, operation: OperationEnum.Operation = None):
        """
        Enable point-to-point handling for this interface.
        """

        point_to_point_ = SubElement(self, 'ipv4-io-cfg:point-to-point')

        if is_not_none(operation):
            point_to_point_.set('xc:operation', operation.value)

    @force_type
    def mtu(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        The IP Maximum Transmission Unit.

        value: int. Range "68..65535"
        """
        mtu_ = SubElement(self, 'ipv4-io-cfg:mtu')

        if is_not_none(value):
            mtu_.text = convert_to_string(value)

        if is_not_none(operation):
            mtu_.set('xc:operation', operation.value)


class IPV4NetworkForwarding(Cfg):

    def __init__(self):
        """ 
        module: Cisco-IOS-XR-ipv4-io-cfg

        Interface IPv4 Network configuration data also used for forwarding
        """

        super().__init__('ipv4-io-cfg:ipv4-network-forwarding')
        self.set('xmlns:ipv4-io-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg')

    def directed_broadcast(self, operation: OperationEnum.Operation = None):
        """
        Enable forwarding of directed broadcast
        """
        directed_broadcast_ = SubElement(self, 'ipv4-io-cfg:directed-broadcast')

        if is_not_none(operation):
            directed_broadcast_.set('xc:operation', operation.value)

    def unreachables(self, operation: OperationEnum.Operation = None):
        """
        Disable sending ICMP unreachables
        """
        unreachables_ = SubElement(self, 'ipv4-io-cfg:unreachables')

        if is_not_none(operation):
            unreachables_.set('xc:operation', operation.value)

    def redirects(self, operation: OperationEnum.Operation = None):
        """
        Enable sending ICMP Redirect messages
        """
        redirects_ = SubElement(self, 'ipv4-io-cfg:redirects')

        if is_not_none(operation):
            redirects_.set('xc:operation', operation.value)


class IPV6QPPBEnum():
    """
    Ipv6 qppb.

    NONE: No QPPB configuration.

    IP_PRECEDENCE: Enable ip-precedence based QPPB.

    QOS_GROUP: Enable qos-group based QPPB.

    BOTH: Enable both ip-precedence and qos-group based QPPB.
    """

    class IPV6QPPB(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    NONE = IPV6QPPB('none')
    IP_PRECEDENCE = IPV6QPPB('ip-precedence')
    QOS_GROUP = IPV6QPPB('qos-group')
    BOTH = IPV6QPPB('both')


class IPV6AccountingEnum():
    """
    Accounting input or output.

    INPUT: Accouting on input.

    OUTPUT: Accouting on output.
    """

    class Accounting(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    INPUT = Accounting('input')
    OUTPUT = Accounting('output')


class IPV6DefaultPingEnum():

    """Ipv6 default ping"""

    class Ipv6DefaultPing(TypeDef):

        """"
        DISABLED: Default route is not allowed to match when checking source address.

        ENABLED: Allow default route to match when checking source address.
        """

        def __init__(self, value):
            super().__init__(value)

    DISABLED = Ipv6DefaultPing('disabled')
    ENABLED = Ipv6DefaultPing('enabled')


class IPV6SelfPingEnum():

    """Ipv6 self ping"""

    class Ipv6SelfPing(TypeDef):
        """"
        DISABLED: Doesn't allow router to ping itself.

        ENABLED: Allow router to ping itself.
        """

        def __init__(self, value):
            super().__init__(value)

    DISABLED = Ipv6SelfPing('disabled')
    ENABLED = Ipv6SelfPing('enabled')


class IPV6ReachableEnum():

    """Ipv6 reachable"""

    class Ipv6Reachable(TypeDef):
        """"
        ANY: Source is reachable via any interface.

        RECEIVED: Source is reachable via interface on which packet was received.
        """

        def __init__(self, value):
            super().__init__(value)

    ANY = Ipv6Reachable('any')
    RECEIVED = Ipv6Reachable('received')


class Ipv6PrefixSid(Cfg):
  
    @force_type
    def __init__(self, prefix_length: int, zone: str = None, route_tag: int = None):
        """
        prefix_length: int: dt1:Ipv6arm-prefix-length. Prefix Length.

        zone: str. IPv6 address zone.

        route_tag: int. RouteTag. range "1..4294967295";
        """

        super().__init__('ipv6-ma-cfg:ipv6-prefix-sid')

        if is_not_none(prefix_length):
            prefix_length_ = SubElement(self, 'ipv6-ma-cfg:prefix-length')
            prefix_length_.text = convert_to_string(prefix_length)
        else:
            raise NoneException()

        if is_not_none(zone):
            zone_ = SubElement(self, 'ipv6-ma-cfg:zone')
            zone_.text = zone

        if is_not_none(route_tag):
            route_tag_ = SubElement(self, 'ipv6-ma-cfg:route-tag')
            route_tag_.text = convert_to_string(route_tag)


class SegmentRouting(Cfg):

    @force_type
    def __init__(self, address: str, ipv6_prefix_sid: Ipv6PrefixSid, operation: OperationEnum.Operation = None):
        """
        Set the IPv6 address of an interface.

        address: str. IPv6 address.

        ipv6_prefix_sid: Prefix.

        enable: Segment Routing Submode.
        """

        super().__init__('ipv6-ma-cfg:segment-routing')

        if is_not_none(ipv6_prefix_sid):
            self.append(ipv6_prefix_sid)

        if is_not_none(address):
            address_ = SubElement(self, 'ipv6-ma-cfg:address')
            address_.text = address
        else:
            raise NoneException('address cannot be None.')

        if is_not_none(operation):
            self.set('xc:operation', operation.value)

    def enable(self):
        SubElement(self.__segment_routing, 'ipv6-ma-cfg:enable')


class SegmentRoutings(Cfg):
    
    @force_type
    def __init__(self):
        """
        Set the IPv6 address of an interface.
        """

        super().__init__('ipv6-ma-cfg:segment-routings')

    def segment_routing(self, segment_routing_: SegmentRouting):
        if is_not_none(segment_routing_):
            self.append(segment_routing_)


class LinkLocalAddress(Cfg):
   

    @force_type
    def __init__(self, address: str, zone: str = None, route_tag: int = None, operation: OperationEnum.Operation = None):
        """
        Indicates a link-local-address node is configured.

        address: str. IPv6 address.

        zone: str. IPv6 address zone.

        route_tag: int. RouteTag. range "1..4294967295"
        """

        super().__init__('ipv6-ma-cfg:link-local-address')

        if is_not_none(address):
            address_ = SubElement(self, 'ipv6-ma-cfg:address')
            address_.text = address
        else:
            raise NoneException('address_ cannot be None.')

        if is_not_none(zone):
            zone_ = SubElement(self, 'ipv6-ma-cfg:zone')
            zone_.text = zone

        if is_not_none(route_tag):
            route_tag_ = SubElement(self, 'ipv6-ma-cfg:route-tag')
            route_tag_.text = convert_to_string(route_tag)

        if is_not_none(operation):
            self.set('xc:operation', operation.value)


class EUI64Addresses(Cfg):

    def __init__(self):
        """
        EUI-64 IPv6 address Table.
        """

        super().__init__('ipv6-ma-cfg:eui64-addresses')

    @force_type
    def eui64_address(self, address: str, prefix_length: int, zone: str = None, route_tag: int = None,
                      operation: OperationEnum.Operation = None):
        """ 
        address: str. IPv6 address.

        prefix_length: int. Prefix Length.

        zone: str. IPv6 address zone.

        route_tag: int. RouteTag. range "1..4294967295".
        """
        eui64_address_ = SubElement(self, 'ipv6-ma-cfg:eui64-address')

        if is_not_none(address):
            address_ = SubElement(eui64_address_, 'ipv6-ma-cfg:address')
            address_.text = address
        else:
            raise NoneException('address cannot be None.')

        if is_not_none(prefix_length):
            prefix_length_ = SubElement(eui64_address_, 'ipv6-ma-cfg:prefix-length')
            prefix_length_.text = convert_to_string(prefix_length)
        else:
            raise NoneException('prefix_length cannot be None.')

        if is_not_none(zone):
            zone_ = SubElement(eui64_address_, 'ipv6-ma-cfg:zone')
            zone_.text = zone

        if is_not_none(route_tag):
            route_tag_ = SubElement(eui64_address_, 'ipv6-ma-cfg:route-tag')
            route_tag_.text = convert_to_string(route_tag)

        if is_not_none(operation):
            eui64_address_.set('xc:operation', operation.value)


class RegularAddresses(Cfg):

    def __init__(self):
        """
        Regular IPv6 address Table.
        """
        super().__init__('ipv6-ma-cfg:regular-addresses')

    @force_type
    def regular_address(self, address: str, prefix_length: int, zone: str = None, route_tag: int = None,
                        operation: OperationEnum.Operation = None):
        """
        address: str. IPv6 address.

        prefix_length: int. Prefix Length.

        zone: str. IPv6 address zone.

        route_tag: int. RouteTag. range "1..4294967295".
        """

        regular_address_ = SubElement(self, 'ipv6-ma-cfg:regular-address')

        if is_not_none(address):
            address_ = SubElement(regular_address_, 'ipv6-ma-cfg:address')
            address_.text = address
        else:
            raise NoneException('address cannot be None.')

        if is_not_none(prefix_length):
            prefix_length_ = SubElement(regular_address_, 'ipv6-ma-cfg:prefix-length')
            prefix_length_.text = convert_to_string(prefix_length)
        else:
            raise NoneException('prefix_length cannot be None.')

        if is_not_none(zone):
            zone_ = SubElement(regular_address_, 'ipv6-ma-cfg:zone')
            zone_.text = zone

        if is_not_none(route_tag):
            route_tag_ = SubElement(regular_address_, 'ipv6-ma-cfg:route-tag')
            route_tag_.text = convert_to_string(route_tag)

        if is_not_none(operation):
            regular_address_.set('xc:operation', operation.value)


class AutoConfiguration(Cfg):

    @force_type
    def __init__(self, operation: OperationEnum.Operation = None):
        """ 
        Auto IPv6 Interface Configuration.

        enable: The flag to enable auto ipv6 interface configuration.

        auto_config_slaac: Enable slaac on Mgmt interface.
        """
        super().__init__('ipv6-ma-cfg:auto-configuration')

        if is_not_none(operation):
            self.set('xc:operation', operation.value)

    def enable(self, operation: OperationEnum.Operation = None):

        enable_ = SubElement(self, 'ipv6-ma-cfg:enable')

        if is_not_none(operation):
            enable_.set('xc:operation', operation.value)

    def auto_config_slaac(self, operation: OperationEnum.Operation = None):

        auto_config_slaac_ = SubElement(self, 'ipv6-ma-cfg:auto-config-slaac')

        if is_not_none(operation):
            auto_config_slaac_.set('xc:operation', operation.value)


class BGPPolicyAccountings(Cfg):
    
    def __init__(self):
        """
        IPv6 BGP Policy Accounting. 
        """
        super().__init__('ipv6-ma-cfg:bgp-policy-accountings')

    @force_type
    def bgp_policy_accounting(self, direction: IPV6AccountingEnum.Accounting, destination_accounting: bool,
                              source_accounting: bool, operation: OperationEnum.Operation = None):
        """
        direction: IPV6AccountingEnum.Accounting. Accouting on input or output.

        destination_accounting: bool. Accounting on Destination IP Address.

        source_accounting: bool. Accounting on Source IP Address.
        """

        bgp_policy_accounting_ = SubElement(self, 'ipv6-ma-cfg:bgp-policy-accounting')

        if is_not_none(direction):
            direction_ = SubElement(bgp_policy_accounting_, 'ipv6-ma-cfg:direction')
            direction_.text = direction.value
        else:
            raise NoneException('direction cannot be None.')

        if is_not_none(destination_accounting):
            destination_accounting_ = SubElement(bgp_policy_accounting_, 'ipv6-ma-cfg:destination-accounting')
            destination_accounting_.text = convert_to_string(destination_accounting)
        else:
            raise NoneException('destination_accounting cannot be None.')

        if is_not_none(source_accounting):
            source_accounting_ = SubElement(bgp_policy_accounting_, 'ipv6-ma-cfg:source-accounting')
            source_accounting_.text = convert_to_string(source_accounting)
        else:
            raise NoneException('source_accounting cannot be None.')

        if is_not_none(operation):
            bgp_policy_accounting_.set('xc:operation', operation.value)


class BgpFlowTagPolicyTable(Cfg):
    
    def __init__(self):
        """
        Interface ipv6 bgp policy propagation flowtag configuration. 
        """
        super().__init__('ipv6-ma-cfg:bgp-flow-tag-policy-table')

    @force_type
    def bgp_flow_tag_policy(self, source: bool = None, destination: bool = None, operation: OperationEnum.Operation = None):
        """
        source: bool. Flow Tag configuration on source. 

        destination: bool. Flow Tag configuration on destination.
        """

        bgp_flow_tag_policy_ = SubElement(self, 'ipv6-ma-cfg:bgp-flow-tag-policy')

        if is_not_none(source):
            source_ = SubElement(bgp_flow_tag_policy_, 'ipv6-ma-cfg:source')
            source_.text = convert_to_string(source)

        if is_not_none(destination):
            destination_ = SubElement(bgp_flow_tag_policy_, 'ipv6-ma-cfg:destination')
            destination_.text = convert_to_string(destination)

        if is_not_none(operation):
            bgp_flow_tag_policy_.set('xc:operation', operation.value)


class IPV6NetworkCfg(Cfg):

    def __init__(self):
        """module: Cisco-IOS-XR-ipv6-ma-cfg"""

        super().__init__('ipv6-ma-cfg:ipv6-network')
        self.set('xmlns:ipv6-ma-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ipv6-ma-cfg')

    @force_type
    def bgp_qos_policy_propagation(self, source: IPV6QPPBEnum.IPV6QPPB = None, destination: IPV6QPPBEnum.IPV6QPPB = None,
                                   operation: OperationEnum.Operation = None):
        """
        Configure BGP QoS policy propagation. Indicates a bgp-qos-policy-propagation node is configured.

        source: IPV6QPPBEnum.IPV6QPPB. QPPB configuration on source.

        destination: IPV6QPPBEnum.IPV6QPPB. QPPB configuration on destination.
        """
        bgp_qos_policy_propagation_ = SubElement(self, 'ipv6-ma-cfg:bgp-qos-policy-propagation')

        if is_not_none(source):
            source_ = SubElement(bgp_qos_policy_propagation_, 'ipv6-ma-cfg:source')
            source_.text = source.value

        if is_not_none(destination):
            destination_ = SubElement(bgp_qos_policy_propagation_, 'ipv6-ma-cfg:destination')
            destination_.text = destination.value

        if is_not_none(operation):
            bgp_qos_policy_propagation_.set('xc:operation', operation.value)

    @force_type
    def bgp_policy_accountings(self, bgp_policy_accountings_: BGPPolicyAccountings):
        """
        IPv6 BGP Policy Accountings. 
        """
        if is_not_none(bgp_policy_accountings_):
            self.append(bgp_policy_accountings_)

    @force_type
    def verify(self, reachable: IPV6ReachableEnum.Ipv6Reachable = None, self_ping: IPV6SelfPingEnum.Ipv6SelfPing = None,
               default_ping: IPV6DefaultPingEnum.Ipv6DefaultPing = None, operation: OperationEnum.Operation = None):
        """ 
        Indicates a verify node is configured.

        reachable: IPV6ReachableEnum.Ipv6Reachable. Source Reachable Interface. 

        self_ping: IPV6SelfPingEnum.Ipv6SelfPing. Allow Self Ping. 

        default_ping: IPV6DefaultPingEnum.Ipv6DefaultPing. Allow Default Route. 
        """
        verify_ = SubElement(self, 'ipv6-ma-cfg:verify')

        if is_not_none(reachable):
            reachable_ = SubElement(verify_, 'ipv6-ma-cfg:reachable')
            reachable_.text = reachable.value

        if is_not_none(self_ping):
            self_ping_ = SubElement(verify_, 'ipv6-ma-cfg:self-ping')
            self_ping_.text = self_ping.value

        if is_not_none(default_ping):
            default_ping_ = SubElement(verify_, 'ipv6-ma-cfg:default-ping')
            default_ping_.text = default_ping.value

        if is_not_none(operation):
            verify_.set('xc:operation', operation.value)

    @force_type
    def addresses(self, segment_routings: SegmentRoutings = None, link_local_address: LinkLocalAddress = None,
                  eui64_addresses: EUI64Addresses = None, regular_addresses: RegularAddresses = None,
                  auto_configuration: AutoConfiguration = None):

        addresses_ = SubElement(self, 'ipv6-ma-cfg:addresses')

        if is_not_none(segment_routings):
            addresses_.append(segment_routings)

        if is_not_none(link_local_address):
            addresses_.append(link_local_address)

        if is_not_none(eui64_addresses):
            addresses_.append(eui64_addresses)

        if is_not_none(regular_addresses):
            addresses_.append(regular_addresses)

        if is_not_none(auto_configuration):
            addresses_.append(auto_configuration)

    @force_type
    def bgp_flow_tag_policy_table(self, bgp_flow_tag_policy_table_: BgpFlowTagPolicyTable):

        if is_not_none(bgp_flow_tag_policy_table_):
            self.append(bgp_flow_tag_policy_table_)

    @force_type
    def mtu(self, mtu: int = None, operation: OperationEnum.Operation = None):
        """ 
        MTU Setting of Interface.

        mtu_: int. range "1280..65535"
        """
        _mtu_ = SubElement(self, 'ipv6-ma-cfg:mtu')

        if is_not_none(mtu):
            _mtu_.text = convert_to_string(mtu)

        if is_not_none(operation):
            _mtu_.set('xc:operation', operation.value)

    @force_type
    def unnumbered(self, unnumbered: str = None, operation: OperationEnum.Operation = None):
        """
        Enable IPv6 processing without an explicit address.

        unnumbered: str. Interface-name.
        """
        _unnumbered_ = SubElement(self, 'ipv6-ma-cfg:unnumbered')

        if is_not_none(unnumbered):
            _unnumbered_.text = unnumbered

        if is_not_none(operation):
            _unnumbered_.set('xc:operation', operation.value)

    @force_type
    def ttl_propagate_disable(self, operation: OperationEnum.Operation = None):
        """
        Disabled TTL propagate on an interface.
        """

        ttl_propagate_disable_ = SubElement(self, 'ipv6-ma-cfg:ttl-propagate-disable')

        if is_not_none(operation):
            ttl_propagate_disable_.set('xc:operation', operation.value)

    @force_type
    def tcp_mss_adjust_enable(self, operation: OperationEnum.Operation = None):
        """
        Enable TCP MSS adjust on an interface
        """
        tcp_mss_adjust_enable_ = SubElement(self, 'ipv6-ma-cfg:tcp-mss-adjust-enable')

        if is_not_none(operation):
            tcp_mss_adjust_enable_.set('xc:operation', operation.value)

    @force_type
    def unreachables(self, operation: OperationEnum.Operation = None):
        """
        Override Sending of ICMP Unreachable Messages
        """
        unreachables_ = SubElement(self, 'ipv6-ma-cfg:unreachables')

        if is_not_none(operation):
            unreachables_.set('xc:operation', operation.value)


class LinkStatusEnum():
    """
    Link status enum

    DEFAULT: Display link status messages for physical links.

    DESABLE: Disable link status messages.

    SOFTWARE_INTERFACES: Display link status messages for all interfaces.
    """

    class LinkStatus(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    DEFAULT = LinkStatus('default')
    DESABLE = LinkStatus('disable')
    SOFTWARE_INTERFACES = LinkStatus('software-interfaces')


class InterfaceCfg(Cfg):

    def __init__(self, tag: str, *args, **kwargs):
        """ module: Cisco-IOS-XR-ifmgr-cfg."""

        super().__init__(tag, *args, **kwargs)
        self.set('xmlns:ifmgr-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg')


class GlobalInterfaceConfigurationCfg(InterfaceCfg):

    def __init__(self):
        """
        Global scoped configuration for interfaces.

        module: Cisco-IOS-XR-ifmgr-cfg.
        """
        super().__init__('ifmgr-cfg:global-interface-configuration')

    @force_type
    def global_interface_configuration(self, link_status: LinkStatusEnum.LinkStatus = None, operation: OperationEnum.Operation = None):
        """link_status: LinkStatusEnum.LinkStatus"""

        link_status_ = SubElement(self, 'ifmgr-cfg:link-status')

        if is_not_none(link_status):
            link_status_.text = convert_to_string(link_status.value)

        if is_not_none(operation):
            link_status_.set('xc:operation', operation.value)


class InterfaceActiveEnum():
    """
    Interface active enum.

    ACIVE: The interface is active.

    PRECONFIGURATION: Preconfiguration.
    """

    class InterfaceActive(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    ACTIVE = InterfaceActive('act')
    PRECONFIGURATION = InterfaceActive('pre')


class InterfaceModeEnum():
    """ 
    Interface mode enum.

    DEFAULT: Default Interface Mode.

    POINT_TO_POINT: Point-to-Point Interface Mode.

    MULTIPOINT: Multipoint Interface Mode.

    L2_TRANSPORT: L2 Transport Interface Mode.
    """

    class InterfaceMode(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    DEFAULT = InterfaceMode('default')
    POINT_TO_POINT = InterfaceMode('point-to-point')
    MULTIPOINT = InterfaceMode('multipoint')
    L2_TRANSPORT = InterfaceMode('l2-transport')


class SecondaryAdminStateEnum():
    """
    Secondary admin state enum.

    NORMAL: Normal Mode.

    MAINTENANCE: Maintenance Mode.
    """

    class SecondaryAdminState(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    NORMAL = SecondaryAdminState('normal')
    MAINTENANCE = SecondaryAdminState('maintenance')


class ArgsDampeningEnum():
    """
    Dampening Arguments

    DEFAULT_VALUES: Default values.

    SPECIFY_HALF_LIFE: Half Life Specified.

    SPECIFY_ALL: All Arguments except Restart Penalty. 

    SPECIFY_RP:  All Arguments Specified.
    """

    class ArgsDampening(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    DEFAULT_VALUES = ArgsDampening('default-values')
    SPECIFY_HALF_LIFE = ArgsDampening('specify-half-life')
    SPECIFY_ALL = ArgsDampening('specify-all')
    SPECIFY_RP = ArgsDampening('specify-rp')


class MTUs(Cfg):

    def __init__(self):
        super().__init__('ifmgr-cfg:mtus')

    @force_type
    def mtu(self, owner: str, mtu: int, operation: OperationEnum.Operation = None):
        """
        The MTU configuration for the interface. 

        owner: str

        mtu: int
        """

        mtu_ = SubElement(self, 'ifmgr-cfg:mtu')

        owner_ = SubElement(mtu_, 'ifmgr-cfg:owner')

        _mtu_ = SubElement(mtu_, 'ifmgr-cfg:mtu')

        if is_not_none(owner):

            owner_.text = owner
        else:
            raise NoneException()

        if is_not_none(mtu):

            _mtu_.text = convert_to_string(mtu)
        else:
            raise NoneException()

        if is_not_none(operation):
            mtu_.set('xc:operation', operation.value)


class InterfaceConfiguration(Cfg):
    
    @force_type
    def __init__(self, active: InterfaceActiveEnum.InterfaceActive, interface_name: str):
        """
        Interface configuration

        module: Cisco-IOS-XR-ifmgr-cfg.

        interface_name: str. The name of the interface.

        active: InterfaceActiveEnum.InterfaceActive. Whether the interface is active or preconfigured.
        """
        super().__init__('ifmgr-cfg:interface-configuration')

        if is_not_none(active):
            active_ = SubElement(self, 'ifmgr-cfg:active')
            active_.text = convert_to_string(active.value)
        else:
            raise NoneException('active can be setted.')

        if is_not_none(interface_name):
            interface_name_ = SubElement(self, 'ifmgr-cfg:interface-name')
            interface_name_.text = interface_name
        else:
            raise NoneException('interface_name cannot be None.')

    @force_type
    def dampening(self, args: ArgsDampeningEnum.ArgsDampening = None, half_life: int = None,
                  reuse_threshold: int = None, suppress_threshold: int = None,
                  suppress_time: int = None, restart_penalty: int = None, operation: OperationEnum.Operation = None):
        """ 
        args: ArgsDampeningEnum.ArgsDampening. Dampening Arguments.

        half_life: args = SPECIFY_HALF_LIFE or args =  SPECIFY_ALL or args = SPECIFY_RP. Decay half life (in minutes). Range "1..45".

        reuse_threshold: args = SPECIFY_ALL or args = SPECIFY_RP. Reuse threshold. Range "1..20000".

        suppress_threshold: args = SPECIFY_ALL or args = SPECIFY_RP. Suppress threshold. Range "1..20000".

        suppress_time: args = SPECIFY_ALL or args = SPECIFY_RP. Max suppress time (in minutes). Range "1..255".

        restart_penalty: args = SPECIFY_RP. Restart penalty. Range "0..20000".
        """

        dampening_ = SubElement(self, 'ifmgr-cfg:dampening')

        if is_not_none(args):
            args_ = SubElement(dampening_, 'ifmgr-cfg:args')
            args_.text = args.value

        if is_not_none(half_life):
            half_life_ = SubElement(dampening_, 'ifmgr-cfg:half-life')
            half_life_.text = convert_to_string(half_life)

        if is_not_none(reuse_threshold):
            reuse_threshold_ = SubElement(dampening_, 'ifmgr-cfg:reuse-threshold')
            reuse_threshold_.text = convert_to_string(reuse_threshold)

        if is_not_none(suppress_threshold):
            suppress_threshold_ = SubElement(dampening_, 'ifmgr-cfg:suppress-threshold')
            suppress_threshold_.text = convert_to_string(suppress_threshold)

        if is_not_none(suppress_time):
            suppress_time_ = SubElement(dampening_, 'ifmgr-cfg:suppress-time')
            suppress_time_.text = convert_to_string(suppress_time)

        if is_not_none(restart_penalty):
            restart_penalty_ = SubElement(dampening_, 'ifmgr-cfg:restart-penalty')
            restart_penalty_.text = convert_to_string(restart_penalty)

        if is_not_none(operation):
            dampening_.set('xc:operation', operation.value)

    def mtus(self, mtus_: MTUs = None):

        if is_not_none(mtus_):
            self.append(mtus_)

    @force_type
    def encapsulation(self, encapsulation_: str = None, capsulation_options: int = None, operation: OperationEnum.Operation = None):
        """
        The encapsulation on the interface.

        encapsulation_ : str. The options for this capsulation, usually '0'

        capsulation_options: int. The encapsulation - e.g. hdlc, ppp
        """
        _encapsulation_ = SubElement(self, 'ifmgr-cfg:encapsulation')

        if is_not_none(encapsulation_):
            _encapsulation = SubElement(_encapsulation_, 'ifmgr-cfg:encapsulation')
            _encapsulation.text = encapsulation_

        if is_not_none(capsulation_options):
            capsulation_options_ = SubElement(_encapsulation_, 'ifmgr-cfg:capsulation-options')
            capsulation_options_.text = convert_to_string(capsulation_options)

        if is_not_none(operation):
            _encapsulation_.set('xc:operation', operation.value)

    def shutdown(self, operation: OperationEnum.Operation = None):
        """
        The existence of this configuration indicates the interface is shut down
        """
        shutdown_ = SubElement(self, 'ifmgr-cfg:shutdown')

        if is_not_none(operation):
            shutdown_.set('xc:operation', operation.value)

    def interface_virtual(self, operation: OperationEnum.Operation = None):
        """
        The mode in which an interface is running. The
        existence of this object causes the creation of
        the software virtual/subinterface.
        """

        interface_virtual_ = SubElement(self, 'ifmgr-cfg:interface-virtual')

        if is_not_none(operation):
            interface_virtual_.set('xc:operation', operation.value)

    @force_type
    def secondary_admin_state(self, value: SecondaryAdminStateEnum.SecondaryAdminState = None,
                              operation: OperationEnum.Operation = None):
        """
        The secondary admin state of the interface

        value: SecondaryAdminStateEnum.
        """
        secondary_admin_state_ = SubElement(
            self, 'ifmgr-cfg:secondary-admin-state')

        if is_not_none(value):
            secondary_admin_state_.text = convert_to_string(value.value)

        if is_not_none(operation):
            secondary_admin_state_.set('xc:operation', operation.value)

    @force_type
    def interface_mode_non_physical(self, value: InterfaceModeEnum.InterfaceMode = None,
                                    operation: OperationEnum.Operation = None):
        """
        The mode in which an interface is running. 
        The existence of this object causes the creation of the software subinterface.

        value: InterfaceModeEnum.
        """

        interface_mode_non_physical_ = SubElement(self, 'ifmgr-cfg:interface-mode-non-physical')

        if is_not_none(value):
            interface_mode_non_physical_.text = value.value

        if is_not_none(operation):
            interface_mode_non_physical_.set('xc:operation', operation.value)

    @force_type
    def bandwidth(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        The bandwidth of the interface in kbps.

        value: int. Range "0..4294967295".
        """

        bandwidth_ = SubElement(self, 'ifmgr-cfg:bandwidth')

        if is_not_none(value):
            bandwidth_.text = convert_to_string(value)

        if is_not_none(operation):
            bandwidth_.set('xc:operation', operation.value)

    def link_status(self, operation: OperationEnum.Operation = None):
        """
        Enable interface and line-protocol state change alarms.
        """

        link_status_ = SubElement(self, 'ifmgr-cfg:link-status')

        if is_not_none(operation):
            link_status_.set('xc:operation', operation.value)

    @force_type
    def description(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        The description of this interface.

        value: str.
        """

        description_ = SubElement(self, 'ifmgr-cfg:description')

        if is_not_none(value):
            description_.text = value

        if is_not_none(operation):
            description_.set('xc:operation', operation.value)

    def ipv4_network(self):
        ipv4_network_ = IPV4NetworkCfg()
        self.append(ipv4_network_)
        return ipv4_network_

    def ipv6_network(self):
        ipv6_network_ = IPV6NetworkCfg()
        self.append(ipv6_network_)
        return ipv6_network_

    def ipv4_network_forwarding(self):
        ipv4_network_forwarding_ = IPV4NetworkForwarding()
        self.append(ipv4_network_forwarding_)
        return ipv4_network_forwarding_


class InterfaceConfigurationsCfg(InterfaceCfg):

    @force_type
    def __init__(self, interface_configuration: InterfaceConfiguration = None):
        """
        Interface configurations

        module: Cisco-IOS-XR-ifmgr-cfg.
        """

        super().__init__('ifmgr-cfg:interface-configurations')
        if is_not_none(interface_configuration):
            self.append(interface_configuration)


class AdminStatusEnum():
    """
    [adapted from IETF interfaces model (RFC 7223)]

        The desired state of the interface.  In RFC 7223 this leaf
        has the same read semantics as ifAdminStatus.  Here, it
        reflects the administrative state as set by enabling or
        disabling the interface.";
        reference "RFC 2863: The Interfaces Group MIB - ifAdminStatus.

    UP: Ready to pass packets.

    DOWN: Not ready to pass packets and not in some test mode.

    TESTING: In some test mode.
    """

    class AdminStatus(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    UP = AdminStatus('UP')
    DOWN = AdminStatus('DOWN')
    TESTING = AdminStatus('TESTING')


class OperStatusEnum():
    """
    [adapted from IETF interfaces model (RFC 7223)]

        The current operational state of the interface.

        This leaf has the same semantics as ifOperStatus.";
    reference "RFC 2863: The Interfaces Group MIB - ifOperStatus

    UP: Ready to pass packets.

    DOWN: The interface does not pass any packets.

    TESTING: In some test mode.  No operational packets can be passed.

    UNKNOWN: Status cannot be determined for some reason.

    DORMANT: Waiting for some external event.

    NOT_PRESENT: Some component (typically hardware) is missing.

    LOWER_LAYER_DOWN: Down due to state of lower-layer interface(s).

    """

    class OperStatus(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    UP = OperStatus('UP')
    DOWN = OperStatus('DOWN')
    TESTING = OperStatus('TESTING')
    UNKNOWN = OperStatus('UNKNOWN')
    DORMANT = OperStatus('DORMANT')
    NOT_PRESENT = OperStatus('NOT_PRESENT')
    LOWER_LAYER_DOWN = OperStatus('LOWER_LAYER_DOWN')


class SubinterfaceOpenConfig(OpenConfig):
   
    @force_type
    def __init__(self, index: int = None):
        """
        index: int. The index of the subinterface, or logical interface number.
        On systems with no support for subinterfaces, or not using
        subinterfaces, this value should default to 0, i.e., the
        default subinterface.
        """
        super().__init__('oc-if:subinterface')

        if is_not_none(index):
            index_ = SubElement(self, 'oc-if:index')
            index_.text = convert_to_string(index)

    @force_type
    def config(self, index: int = None, name: str = None, description: str = None, enabled: bool = None):

        config_ = SubElement(self, 'oc-if:config')

        if is_not_none(index):
            index_ = SubElement(config_, 'oc-if:index')
            index_.text = convert_to_string(index)

        if is_not_none(name):
            name_ = SubElement(config_, 'oc-if:name')
            name_.text = name

        if is_not_none(description):
            description_ = SubElement(config_, 'oc-if:description')
            description_.text = description

        if is_not_none(enabled):
            enabled_ = SubElement(config_, 'oc-if:enabled')
            enabled_.text = convert_to_string(enabled)


class SubinterfacesOpenConfig(OpenConfig):

    @force_type
    def __init__(self):
        super().__init__('oc-if:subinterfaces')

    def subinterface(self, subinterface: SubinterfaceOpenConfig = None):

        if is_not_none(subinterface):
            self.append(subinterface)


class InterfaceOpenConfig(OpenConfig):
    
    @force_type
    def __init__(self, name: str):
        """
        name: str.
        """
        super().__init__('oc-if:interface')

        if is_not_none(name):
            name_ = SubElement(self, 'oc-if:name')
            name_.text = name
        else:
            raise NoneException('name cannot be None.')

    @force_type
    def config(self, type_: str, mtu: int = None, name: str = None, description: str = None, enabled: bool = None):
        """ 
        type_: str. [adapted from IETF interfaces model (RFC 7223)]

        The type of the interface.

        When an interface entry is created, a server MAY
        initialize the type leaf with a valid value, e.g., if it
        is possible to derive the type from the name of the
        interface.

        If a client tries to set the type of an interface to a
        value that can never be used by the system, e.g., if the
        type is not supported or if the type does not match the
        name of the interface, the server MUST reject the request.
        A NETCONF server MUST reply with an rpc-error with the
        error-tag 'invalid-value' in this case.";
        reference "RFC 2863: The Interfaces Group MIB - ifType.

        mtu: int. Set the max transmission unit size in octets
        for the physical interface.  If this is not set, the mtu is
        set to the operational default -- e.g., 1514 bytes on an
        Ethernet interface.


        name: str. [adapted from IETF interfaces model (RFC 7223)]

         The name of the interface.

        A device MAY restrict the allowed values for this leaf,
        possibly depending on the type of the interface.
        For system-controlled interfaces, this leaf is the
        device-specific name of the interface.  The 'config false'
        list interfaces/interface[name]/state contains the currently
        existing interfaces on the device.

        If a client tries to create configuration for a
        system-controlled interface that is not present in the
        corresponding state list, the server MAY reject
        the request if the implementation does not support
        pre-provisioning of interfaces or if the name refers to
        an interface that can never exist in the system.  A
        NETCONF server MUST reply with an rpc-error with the
        error-tag 'invalid-value' in this case.

        The IETF model in RFC 7223 provides YANG features for the
        following (i.e., pre-provisioning and arbitrary-names),
        however they are omitted here:

          If the device supports pre-provisioning of interface
          configuration, the 'pre-provisioning' feature is
          advertised.

        If the device allows arbitrarily named user-controlled
        interfaces, the 'arbitrary-names' feature is advertised.

        When a configured user-controlled interface is created by
        the system, it is instantiated with the same name in the
        /interfaces/interface[name]/state list.";
        reference "RFC 7223: A YANG Data Model for Interface Management";



        description: str. [adapted from IETF interfaces model (RFC 7223)]

        A textual description of the interface.

        A server implementation MAY map this leaf to the ifAlias
        MIB object.  Such an implementation needs to use some
        mechanism to handle the differences in size and characters
        allowed between this leaf and ifAlias.  The definition of
        such a mechanism is outside the scope of this document.

        Since ifAlias is defined to be stored in non-volatile
        storage, the MIB implementation MUST map ifAlias to the
        value of 'description' in the persistently stored
        datastore.

        Specifically, if the device supports ':startup', when
        ifAlias is read the device MUST return the value of
        'description' in the 'startup' datastore, and when it is
        written, it MUST be written to the 'running' and 'startup'
        datastores.  Note that it is up to the implementation to

        decide whether to modify this single leaf in 'startup' or
        perform an implicit copy-config from 'running' to
        'startup'.

        If the device does not support ':startup', ifAlias MUST
        be mapped to the 'description' leaf in the 'running'
        datastore.";
        reference "RFC 2863: The Interfaces Group MIB - ifAlias";

        enabled: bool. [adapted from IETF interfaces model (RFC 7223)]

        This leaf contains the configured, desired state of the
        interface.

        Systems that implement the IF-MIB use the value of this
        leaf in the 'running' datastore to set
        IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
        has been initialized, as described in RFC 2863.

        Changes in this leaf in the 'running' datastore are
        reflected in ifAdminStatus, but if ifAdminStatus is
        changed over SNMP, this leaf is not affected.";
        reference "RFC 2863: The Interfaces Group MIB - ifAdminStatus";
        """
        config_ = SubElement(self, 'oc-if:config')

        if is_not_none(type_):
            _type_ = SubElement(config_, 'oc-if:type')
            _type_.set('xmlns:idx', 'urn:ietf:params:xml:ns:yang:iana-if-type')
            _type_.text = type_
        else:
            raise NoneException('type_ cannot be None.')

        if is_not_none(mtu):
            mtu_ = SubElement(config_, 'oc-if:mtu')
            mtu_.text = convert_to_string(mtu)

        if is_not_none(name):
            name_ = SubElement(config_, 'oc-if:name')
            name_.text = name

        if is_not_none(description):
            description_ = SubElement(config_, 'oc-if:description')
            description_.text = description

        if is_not_none(enabled):
            enabled_ = SubElement(config_, 'oc-if:enabled')
            enabled_.text = convert_to_string(enabled)

    @force_type
    def hold_time(self, up: int = None, down: int = None):

        hold_time = SubElement(self, 'oc-if:hold-time')

        config = SubElement(hold_time, 'oc-if:config')

        if is_not_none(up):
            up_ = SubElement(config, 'oc-if:up')
            up_.text = convert_to_string(up)

        if is_not_none(down):
            down_ = SubElement(config, 'oc-if:down')
            down_.text = convert_to_string(down)

    @force_type
    def subinterfaces(self, subinterfaces=SubinterfacesOpenConfig()):

        if is_not_none(subinterfaces):
            self.append(subinterfaces)


class OpenConfigInterfaces(OpenConfig):

    def __init__(self):
        """
        module: openconfig-interfaces.
        """
        super().__init__('oc-if:interfaces')
        self.set('xmlns:oc-if', 'http://openconfig.net/yang/interfaces')

    @force_type
    def interface(self, interface: InterfaceOpenConfig = None):

        if is_not_none(interface):
            self.append(interface)
